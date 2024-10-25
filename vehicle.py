# vehicle class

class Vehicle:
    def __init__(self, model, vehicle_number):
        self.__model = model
        self.__vehicle_number = vehicle_number

    
    def vehicleDetails(self):
        return [self.model ,self.vehicle_number]
    
    def get_model(self):
        return self.__model
    
    def set_model(self, new_model):
        self.__model = new_model

    def get_vehicle_number(self):
        return self.__vehicle_number