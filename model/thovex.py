from car import Car
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine

class Thovex(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage):
        super.__init__(NubbinBattery(last_service_date), CapuletEngine(last_service_mileage, current_mileage))