import smtplib
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
import os

from app.main import db

API_KEY = os.environ.get('API_KEY')
API_URL = 'https://holidays.abstractapi.com/v1/'


def fetch_public_holidays(api_key: str, country: str, year: str = None, month: str = None, day: str = None):
    params = {
        'api_key': api_key,
        'country': country
    }
    if year:
        params['year'] = year
    if month:
        params['month'] = month
    if day:
        params['day'] = day

    response = requests.get(API_URL, params=params)
    return response.json()


def send_email(subject: str, body: str, to_email: str) -> None:
    from_email = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')

    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())


def email_public_holidays_for_upcoming_month() -> None:

    employees = db.list_employees()
    for employee in employees:
        start_date = datetime.today().strftime('%Y-%m-%d')
        end_date = (datetime.today() + timedelta(days=30)).strftime('%Y-%m-%d')

        public_holidays = fetch_public_holidays(employee.residence_location, start_date, end_date)
        holidays_text = "\n".join([holiday['name'] for holiday in public_holidays])

        subject = "Upcoming Public Holidays For Next Month"
        body = f"Hello {employee.name},\n\nHere are the public holidays for the upcoming month:\n{holidays_text}"
        send_email(subject, body, employee.email)
