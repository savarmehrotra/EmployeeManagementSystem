from typing import Optional

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Employee(BaseModel):
    employee_id: UUID
    name: str
    position: str
    email: str
    salary: float
    created_at: datetime
    modified_at: datetime


class CreateEmployeeRequest(BaseModel):
    name: str
    position: str
    email: str
    salary: float


class UpdateEmployeeRequest(BaseModel):
    name: Optional[str] = None
    position: Optional[str] = None
    email: Optional[str] = None
    salary: Optional[float] = None
