from abc import ABC, abstractclassmethod

class Engine(ABC):
    @abstractclassmethod
    def needs_service(self):
        pass