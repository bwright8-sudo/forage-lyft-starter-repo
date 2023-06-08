from car import Car
from battery.spindler_battery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine

class Glissade(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage):
        super.__init__(SpindlerBattery(last_service_date), WilloughbyEngine(last_service_mileage, current_mileage))