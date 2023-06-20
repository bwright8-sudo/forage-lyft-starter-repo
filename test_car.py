import unittest
from datetime import datetime, date

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tires import CarriginTires
from tire.octoprime_tires import OctoprimeTires

class TestCapulet(unittest.TestCase):
    def test_capulet_needs_service(self):
        last_service_mileage = 20000
        current_mileage = 55000
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_needs_service_2(self):
        last_service_mileage = 0
        current_mileage = 30000
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 29999
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

    def test_capulet_does_not_need_service_2(self):
        last_service_mileage = 20000
        current_mileage = 40000
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_willoughby_needs_service(self):
        last_service_mileage = 20000
        current_mileage = 85000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_needs_service_2(self):
        last_service_mileage = 0
        current_mileage = 60000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 59999
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

    def test_willoughby_does_not_need_service_2(self):
        last_service_mileage = 20000
        current_mileage = 70000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_sternman_needs_service(self):
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_does_not_need_service(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())

class TestSpindler(unittest.TestCase):
    def test_spindler_needs_service(self):
        last_service_date = date(2019, 8, 17)
        engine = SpindlerBattery(last_service_date)
        self.assertTrue(engine.needs_service())

    def test_spindler_needs_service_2(self):
        last_service_date = date(2020, 6, 20)
        engine = SpindlerBattery(last_service_date)
        self.assertTrue(engine.needs_service())

    def test_spindler_does_not_need_service(self):
        last_service_date = date(2020, 6, 21)
        engine = SpindlerBattery(last_service_date)
        self.assertFalse(engine.needs_service())

    def test_spindler_does_not_need_service_2(self):
        last_service_date = date(2022, 9, 6)
        engine = SpindlerBattery(last_service_date)
        self.assertFalse(engine.needs_service())

class TestNubbin(unittest.TestCase):
    def test_nubbin_needs_service(self):
        last_service_date = date(2018, 8, 17)
        engine = NubbinBattery(last_service_date)
        self.assertTrue(engine.needs_service())

    def test_nubbin_needs_service_2(self):
        last_service_date = date(2019, 6, 20)
        engine = NubbinBattery(last_service_date)
        self.assertTrue(engine.needs_service())

    def test_nubbin_does_not_need_service(self):
        last_service_date = date(2019, 6, 21)
        engine = NubbinBattery(last_service_date)
        self.assertFalse(engine.needs_service())

    def test_nubbin_does_not_need_service_2(self):
        last_service_date = date(2022, 6, 9)
        engine = NubbinBattery(last_service_date)
        self.assertFalse(engine.needs_service())

class TestCarrigan(unittest.TestCase):
    def test_carrigan_needs_service(self):
        wear_sensor_results = [1, 0.8, 0.3, 0.5]
        tires = CarriginTires(wear_sensor_results)
        self.assertTrue(tires.needs_service())

    def test_carrigan_needs_service_2(self):
        wear_sensor_results = [0.9, 0.2, 0.5, 0.8]
        tires = CarriginTires(wear_sensor_results)
        self.assertTrue(tires.needs_service())

    def test_carrigan_does_not_need_service(self):
        wear_sensor_results = [0.89, 0.64, 0.5, 0.1]
        tires = CarriginTires(wear_sensor_results)
        self.assertFalse(tires.needs_service())

    def test_carrigan_does_not_need_service_2(self):
        wear_sensor_results = [0.1, 0.234, 0.7, 0.3]
        tires = CarriginTires(wear_sensor_results)
        self.assertFalse(tires.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_octoprime_needs_service(self):
        wear_sensor_results = [1, 0.8, 0.9, 0.5]
        tires = OctoprimeTires(wear_sensor_results)
        self.assertTrue(tires.needs_service())

    def test_octoprime_needs_service_2(self):
        wear_sensor_results = [1, 1, 0.5, 0.5]
        tires = OctoprimeTires(wear_sensor_results)
        self.assertTrue(tires.needs_service())

    def test_octoprime_does_not_need_service(self):
        wear_sensor_results = [1, 0.4, 0.5, 1]
        tires = OctoprimeTires(wear_sensor_results)
        self.assertFalse(tires.needs_service())

    def test_octoprime_does_not_need_service_2(self):
        wear_sensor_results = [0.1, 0.234, 0.7, 0.3]
        tires = OctoprimeTires(wear_sensor_results)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
