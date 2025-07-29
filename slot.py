# slot.py

class ParkingSlot:
    def __init__(self, slot_id, slot_type):
        self.slot_id = slot_id
        self.slot_type = slot_type.lower()  # compact, suv, two_wheeler
        self.is_occupied = False
        self.parked_vehicle = None

    def park_vehicle(self, vehicle):
        if not self.is_occupied and vehicle.vehicle_type == self.slot_type:
            self.parked_vehicle = vehicle
            self.is_occupied = True
            return True
        return False

    def unpark_vehicle(self):
        if self.is_occupied:
            vehicle = self.parked_vehicle
            self.parked_vehicle = None
            self.is_occupied = False
            return vehicle
        return None

    def __str__(self):
        status = "Occupied" if self.is_occupied else "Available"
        return f"{self.slot_id} [{self.slot_type.replace('_', ' ').title()}] - {status}"
