from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID
from app.models.employee_models import Employee, CreateEmployeeRequest, UpdateEmployeeRequest


class EmployeeRepository(ABC):
    @abstractmethod
    def add_employee(self, employee_create: CreateEmployeeRequest) -> Employee:
        pass

    @abstractmethod
    def update_employee(self, employee_id: UUID, employee_update: UpdateEmployeeRequest) -> Optional[Employee]:
        pass

    @abstractmethod
    def get_employee(self, employee_id: UUID) -> Optional[Employee]:
        pass

    @abstractmethod
    def delete_employee(self, employee_id: UUID) -> bool:
        pass

    @abstractmethod
    def list_employees(self) -> List[Employee]:
        pass
