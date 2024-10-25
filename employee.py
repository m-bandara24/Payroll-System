# Employee parent class

class Employee:
    def __init__(self, first_name, last_name, employee_id, work_type, wage):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__employee_id = employee_id
        self.__work_type = work_type
        self.__wage = wage

    def calculate_salary(self):
        pass  # To be overridden in subclasses

    def tax_deduction(self, amount, tax_rate):
        return amount * (1 - tax_rate)
    
    def employeeDetails(self):
        return [self.__first_name, self.__last_name, self.__employee_id, self.__work_type, self.__wage]
    
    def display_details(self):
        return f"ID: {self.__employee_id}, Name: {self.__first_name} {self.__last_name}, Work Type: {self.__work_type}, Wage: {self.__wage}"

    def get_employee_id(self):
        return self.__employee_id

    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name

    def get_work_type(self):
        return self.__work_type

    def get_wage(self):
        return self.__wage

    def set_wage(self, wage):
        self.__wage = wage
