from abc import ABC, abstractclassmethod

class Tire(ABC):
    def __init__(self, wear_sensor_results):
        self.number_of_tires = 4
        self.wear_sensor_results = wear_sensor_results
    
    @abstractclassmethod
    def needs_service(self):
        pass