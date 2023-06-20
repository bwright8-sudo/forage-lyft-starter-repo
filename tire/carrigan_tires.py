from tire.tire import Tire

class CarriginTires(Tire):
    def __init__(self, wear_sensor_results):
        self.wear_service_threshold = 0.9
        super().__init__(wear_sensor_results)

    def needs_service(self):
        for i in range(self.number_of_tires):
            if (self.wear_sensor_results[i] >= self.wear_service_threshold):
                return True
        return False

    

