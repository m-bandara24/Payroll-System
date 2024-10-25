# intern class

from employee import Employee
from vehicle import Vehicle

class Intern(Employee):
    def __init__(self, first_name, last_name, employee_id, vehicle):
        super().__init__(first_name, last_name, employee_id, 'I', 1000.00)
        self.__stipend = 1000.00
        self.vehicle_model = vehicle.get_model()
        self.vehicle_number = vehicle.get_vehicle_number()

    def calculate_salary(self):
        return self.__stipend  # No tax deduction for interns
