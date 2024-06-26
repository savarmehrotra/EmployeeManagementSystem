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