import re
from app.exceptions.employee_exceptions import InvalidEmailFormatException


def validate_email_format(email: str) -> bool:
    """
    Validates the format of the email using a regular expression.

    Args:
        email (str): The email to be validated.

    Returns:
        bool: True if the email format is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(email_regex, email):
        raise InvalidEmailFormatException(email)
    return True
