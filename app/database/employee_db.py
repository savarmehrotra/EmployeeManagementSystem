from uuid import UUID, uuid4
from datetime import datetime
from typing import List, Optional
from app.models.employee_models import Employee, CreateEmployeeRequest, UpdateEmployeeRequest
from app.database.employee_respository import EmployeeRepository


class EmployeeDatabase(EmployeeRepository):
    def __init__(self):
        self.employees = []

    def add_employee(self, employee_create: CreateEmployeeRequest) -> Employee:
        employee_id = uuid4()
        now = datetime.utcnow()
        employee = Employee(
            employee_id=employee_id,
            name=employee_create.name,
            position=employee_create.position,
            email=employee_create.email,
            salary=employee_create.salary,
            created_at=now,
            modified_at=now
        )
        self.employees.append(employee)
        return employee

    def update_employee(self, employee_id: UUID, employee_update: UpdateEmployeeRequest) -> Optional[Employee]:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                if employee_update.name is not None:
                    employee.name = employee_update.name
                if employee_update.position is not None:
                    employee.position = employee_update.position
                if employee_update.email is not None:
                    employee.email = employee_update.email
                if employee_update.salary is not None:
                    employee.salary = employee_update.salary
                employee.modified_at = datetime.utcnow()
                return employee
        return None

    def get_employee(self, employee_id: UUID) -> Optional[Employee]:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def delete_employee(self, employee_id: UUID) -> bool:
        for index, employee in enumerate(self.employees):
            if employee.employee_id == employee_id:
                del self.employees[index]
                return True
        return False

    def list_employees(self) -> List[Employee]:
        return self.employees
