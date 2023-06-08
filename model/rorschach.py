from car import Car
from battery.nubbin_battery import NubbinBattery
from engine.willoughby_engine import WilloughbyEngine

class Rorschach(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage):
        super.__init__(NubbinBattery(last_service_date), WilloughbyEngine(last_service_mileage, current_mileage))