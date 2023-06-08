from serviceable import Serviceable
from engine.mileage_engine import MileageEngine
from battery.battery import Battery

class Car(Serviceable):
    def __init__(self, battery, engine):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
