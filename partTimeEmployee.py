# part time class

from employee import Employee
from vehicle import Vehicle

class PartTimeEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, hourly_rate, hours_worked, vehicle):
        super().__init__(first_name, last_name, employee_id, 'P', hourly_rate * hours_worked)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked
        self.vehicle_model = vehicle.get_model()
        self.vehicle_number = vehicle.get_vehicle_number()

    def calculate_salary(self):
        gross_salary = self.__hourly_rate * self.__hours_worked
        net_salary = self.tax_deduction(gross_salary, 0.15)
        return net_salary
