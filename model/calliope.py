from car import Car
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine

class Calliope(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage):
        super.__init__(SpindlerBattery(last_service_date), CapuletEngine(last_service_mileage, current_mileage))