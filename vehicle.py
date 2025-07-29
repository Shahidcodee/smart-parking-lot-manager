from abc import ABC, abstractmethod
from datetime import datetime

class Vehicle(ABC):
    def __init__(self, license_plate: str):
        self.license_plate = license_plate
        self.entry_time = datetime.now()

    @abstractmethod
    def get_type(self):
        pass

class Car(Vehicle):
    def get_type(self):
        return "car"

class Bike(Vehicle):
    def get_type(self):
        return "bike"
