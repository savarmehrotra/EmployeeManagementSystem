from uuid import UUID


class EmployeeNotFoundException(Exception):
    def __init__(self, employee_id: UUID = None):
        if employee_id:
            self.message = f"Employee with ID {employee_id} not found"
        else:
            self.message = "Employee not found"
        super().__init__(self.message)


class InvalidEmailFormatException(Exception):
    def __init__(self, email: str):
        self.message = f"Invalid email format: {email}"
        super().__init__(self.message)


class NoEmployeeFoundException(Exception):
    def __init__(self):
        self.message = "No employees found"
        super().__init__(self.message)
