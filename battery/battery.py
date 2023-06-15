from abc import ABC
from datetime import datetime

class Battery(ABC):
    def __init__(self, last_service_date, yearly_service_frequency):
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()
        self.yearly_service_frequency = yearly_service_frequency

    def needs_service(self):
        return self.last_service_date.replace(year=self.last_service_date.year + self.yearly_service_frequency) <= self.current_date