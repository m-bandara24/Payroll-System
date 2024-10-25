# full time employee child class

from employee import Employee
from vehicle import Vehicle

class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, monthly_salary, vehicle):
        super().__init__(first_name, last_name, employee_id, 'F', monthly_salary)
        self.__monthly_salary = monthly_salary
        self.vehicle_model = vehicle.get_model()
        self.vehicle_number = vehicle.get_vehicle_number()

    def calculate_salary(self):
        net_salary = self.tax_deduction(self.__monthly_salary, 0.18)
        return net_salary
