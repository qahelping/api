from helpers.base_service import BaseService


class EmployeeService(BaseService):
    BASE_URL = "https://dummy.restapiexample.com/api/v1/employees"

    def get_employee(self):
        response = self.get(self.BASE_URL)
        return response