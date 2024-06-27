from typing import List

from fastapi import FastAPI, HTTPException
from uuid import UUID

from app.database.employee_db import EmployeeDatabase
from app.exceptions.employee_exceptions import EmployeeNotFoundException, InvalidEmailFormatException
from app.models.employee_models import Employee, CreateEmployeeRequest, UpdateEmployeeRequest
from app.utils.email_validators import validate_email_format
from app.utils.time_utils import transform_to_local_time

app = FastAPI()
db = EmployeeDatabase()


@app.post("/employees/", response_model=Employee)
def create_employee(create_employee_request: CreateEmployeeRequest) -> Employee:
    """
    Creates a new employee with the provided details.

    Args:
        create_employee_request (CreateEmployeeRequest): Details of the employee to be created.

    Returns:
        Employee: The created employee.

    Raises:
        HTTPException: If the email format is invalid (400 Bad Request).
    """
    try:
        validate_email_format(create_employee_request.email)
        new_employee = db.add_employee(create_employee_request)
        print(f"Employee created: {new_employee}")
        return new_employee
    except InvalidEmailFormatException as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/employees/{employee_id}/", response_model=Employee)
def update_employee(employee_id: UUID, update_employee_request: UpdateEmployeeRequest) -> Employee:
    """
    Updates an existing employee with the provided details.

    Args:
        employee_id (UUID): The ID of the employee to update.
        update_employee_request (UpdateEmployeeRequest): Updated details of the employee.

    Returns:
        Employee: The updated employee.

    Raises:
        HTTPException: If the employee with the given ID is not found (404 Not Found).
        HTTPException: If the email format is invalid (400 Bad Request).
    """
    try:
        validate_email_format(update_employee_request.email)
        updated_employee = db.update_employee(update_employee_request)
        if not updated_employee:
            raise EmployeeNotFoundException(employee_id)
        print(f"Employee updated: {updated_employee}")
        return updated_employee
    except InvalidEmailFormatException as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/employees/{employee_id}/", response_model=Employee)
def get_employee(employee_id: UUID) -> Employee:
    """
    Retrieves an employee by their ID.

    Args:
        employee_id (UUID): The ID of the employee to retrieve.

    Returns:
        Employee: The retrieved employee with timestamps in local time.

    Raises:
        HTTPException: If the employee with the given ID is not found (404 Not Found).
    """
    try:
        employee = db.get_employee(employee_id=employee_id)
        if not employee:
            raise EmployeeNotFoundException(employee_id)

        # Transform timestamps to local time
        employee.created_at = transform_to_local_time(employee.created_at)
        employee.modified_at = transform_to_local_time(employee.modified_at)

        print(f"Employee retrieved: {employee}")
        return employee
    except EmployeeNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/employees/", response_model=List[Employee])
def get_all_employees() -> List[Employee]:
    """
    Fetches all employees from the database.

    Returns:
        List[Employee]: A list of all employees with timestamps in local time.

    Raises:
        HTTPException: If no employees are found (404 Not Found).
    """
    try:
        employees = db.list_employees()
        if not employees:
            raise EmployeeNotFoundException()

        # Transform timestamps to local time for all employees
        for employee in employees:
            employee.created_at = transform_to_local_time(employee.created_at)
            employee.modified_at = transform_to_local_time(employee.modified_at)

        print(f"All employees retrieved: {employees}")
        return employees
    except EmployeeNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/email_public_holidays")
def trigger_email_public_holidays():
    return {"message": "Emails for upcoming public holidays will be sent shortly."}
