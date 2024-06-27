# Employee Management System

Simple Employee Database Management System that allows adding new employees and retrieving information about existing employees.


## Setup Instructions

### Prerequisites
- Python 3.8+
- Poetry


### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/savarmehrotra/EmployeeManagementSystem.git
   cd EmployeeManagementSystem
   ```

2. Install dependencies:
   ```sh
   poetry install
   ```

### Running the Application

1. **Get Your API Key**
   - Create an API key from [Abstract API Holidays API](https://www.abstractapi.com/api/holidays-api).

2. **Note your email id and password from which you want to send the public holidays email**

3. 3**Set Environment Variables**
   ```sh
   export API_KEY="your_abstract_api_key"
   export EMAIL_USERNAME="your_email@example.com"
   export EMAIL_PASSWORD="your_email_password"
Replace "your_abstract_api_key", "your_email@example.com", and "your_email_password" with your actual credentials.


To run the FastAPI application, use the following command:
```sh
poetry run uvicorn app.main:app --reload
```

### FastAPI Endpoints

#### Create Employee
```sh
curl -X POST "http://localhost:8000/employees/" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "John Doe",
        "position": "Software Engineer",
        "email": "john.doe@example.com",
        "salary": 75000
    }'
```

#### Get All Employees
```sh
curl -X GET "http://localhost:8000/employees/" \
    -H "Accept: application/json"
```

#### Get Employee by ID
```sh
curl -X GET "http://localhost:8000/employees/{employee_id}" \
    -H "Accept: application/json"
```

#### Update Employee
```sh
curl -X PUT "http://localhost:8000/employees/{employee_id}" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Jane Smith",
        "position": "Project Manager",
        "email": "jane.smith@example.com",
        "salary": 85000
    }'
```

#### Trigger Email Notifications for Public Holidays
```sh
curl -X GET "http://localhost:8000/email_public_holidays" \
    -H "Accept: application/json"
```