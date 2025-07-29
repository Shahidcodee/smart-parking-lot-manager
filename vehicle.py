# vehicle.py

import datetime

class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate.upper()
        self.vehicle_type = vehicle_type.lower()
        self.entry_time = datetime.datetime.now()

    def __str__(self):
        return f"{self.license_plate} ({self.vehicle_type}) - Entered at {self.entry_time.strftime('%Y-%m-%d %H:%M:%S')}"