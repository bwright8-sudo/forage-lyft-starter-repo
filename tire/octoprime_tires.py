from tire.tire import Tire

class OctoprimeTires(Tire):
    def __init__(self, wear_sensor_results):
        self.wear_service_threshold = 3
        super().__init__(wear_sensor_results)

    def needs_service(self):
        wear_values_sum = 0
        for i in range(self.number_of_tires):
            wear_values_sum += self.wear_sensor_results[i]

            if (wear_values_sum >= self.wear_service_threshold):
                return True
        return False