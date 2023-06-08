from car import Car
from battery.spindler_battery import SpindlerBattery
from engine.sternman_engine import SternmanEngine

class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_on):
        super.__init__(SpindlerBattery(last_service_date), SternmanEngine(warning_light_on))