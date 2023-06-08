from abc import ABC
from engine.engine import Engine

class MileageEngine(Engine, ABC):
    def __init__(self, last_service_mileage, current_mileage, mileage_service_frequency):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.mileage_service_frequency = mileage_service_frequency

    def needs_service(self):
        return (self.current_mileage - self.last_service_mileage) > self.mileage_service_frequency