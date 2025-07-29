# parking_lot.py

from slot import ParkingSlot
from vehicle import Vehicle
import datetime

class ParkingLot:
    def __init__(self):
        self.slots = []
        self.vehicle_map = {}
        self.setup_slots()

    def setup_slots(self):
        # 4 slots each for compact, suv, two_wheeler
        for i in range(1, 5):
            self.slots.append(ParkingSlot(f"C{i}", "compact"))
            self.slots.append(ParkingSlot(f"S{i}", "suv"))
            self.slots.append(ParkingSlot(f"T{i}", "two_wheeler"))

    def show_available_slots(self):
        print("\n📍 Available Slots:")
        found = False
        for slot in self.slots:
            if not slot.is_occupied:
                print(slot)
                found = True
        if not found:
            print("❌ No slots available.")

    def park_vehicle(self, license_plate, vehicle_type):
        license_plate = license_plate.upper()
        if license_plate in self.vehicle_map:
            print("⚠️ This vehicle is already parked.")
            return

        vehicle = Vehicle(license_plate, vehicle_type)
        for slot in self.slots:
            if slot.slot_type == vehicle.vehicle_type and not slot.is_occupied:
                if slot.park_vehicle(vehicle):
                    self.vehicle_map[license_plate] = slot
                    print(f"✅ Vehicle parked at slot {slot.slot_id}")
                    return
        print("❌ No available slot for this vehicle type.")

    def unpark_vehicle(self, license_plate):
        license_plate = license_plate.upper()
        if license_plate not in self.vehicle_map:
            print("❌ Vehicle not found.")
            return

        slot = self.vehicle_map[license_plate]
        vehicle = slot.unpark_vehicle()
        if vehicle:
            duration = datetime.datetime.now() - vehicle.entry_time
            hours = max(1, int(duration.total_seconds() // 3600))
            rate = self.get_rate(vehicle.vehicle_type)
            cost = hours * rate
            print(f"✅ Vehicle {vehicle.license_plate} unparked from Slot {slot.slot_id}")
            print(f"⏱️ Duration: {hours} hour(s)")
            print(f"💰 Total Charges: ₹{cost}")
            del self.vehicle_map[license_plate]
        else:
            print("❌ Error during unparking.")

    def get_rate(self, vehicle_type):
        rates = {
            "compact": 30,
            "suv": 50,
            "two_wheeler": 10
        }
        return rates.get(vehicle_type, 30)

    def search_vehicle(self, license_plate):
        license_plate = license_plate.upper()
        if license_plate in self.vehicle_map:
            slot = self.vehicle_map[license_plate]
            print(f"🔍 Vehicle {license_plate} is parked at Slot {slot.slot_id}")
        else:
            print("❌ Vehicle not found.")
