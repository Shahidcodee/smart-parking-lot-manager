class ParkingSlot:
    def __init__(self, slot_id: str, slot_type: str):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.is_occupied = False
        self.vehicle = None

    def park(self, vehicle):
        self.is_occupied = True
        self.vehicle = vehicle

    def unpark(self):
        self.is_occupied = False
        v = self.vehicle
        self.vehicle = None
        return v
