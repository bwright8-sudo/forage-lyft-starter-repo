from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        self.yearly_service_frequency = 4
        super().__init__(last_service_date, self.yearly_service_frequency)