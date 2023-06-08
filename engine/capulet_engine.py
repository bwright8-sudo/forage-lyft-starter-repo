from engine.mileage_engine import MileageEngine

class CapuletEngine(MileageEngine):
    def __init__(self, last_service_mileage, current_mileage):
        self.mileage_service_frequency = 30000
        super().__init__(last_service_mileage, current_mileage, self.mileage_service_frequency) 