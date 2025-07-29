from vehicle import Car, Bike
from slot import ParkingSlot
from storage import save_data, load_data
from utils import log_activity
from datetime import datetime

class ParkingLotManager:
    def __init__(self):
        self.slots = load_data()
        if not self.slots:
            self.setup_slots()

    def setup_slots(self):
        self.slots = []
        for i in range(1, 5):
            self.slots.append(ParkingSlot(f"C{i}", "car"))
            self.slots.append(ParkingSlot(f"B{i}", "bike"))

    def find_free_slot(self, vehicle_type):
        for slot in self.slots:
            if slot.slot_type == vehicle_type and not slot.is_occupied:
                return slot
        return None

    def park_vehicle(self):
        license_plate = input("Enter vehicle license plate: ").strip()
        vtype = input("Enter vehicle type (car/bike): ").strip().lower()
        if vtype not in ['car', 'bike']:
            print("Invalid vehicle type.")
            return
        vehicle = Car(license_plate) if vtype == 'car' else Bike(license_plate)

        slot = self.find_free_slot(vtype)
        if not slot:
            print(f"No free {vtype} slots available.")
            return

        slot.park(vehicle)
        save_data(self.slots)
        log_activity(f"Vehicle {license_plate} parked in slot {slot.slot_id}.")
        print(f"Vehicle parked in slot {slot.slot_id} at {vehicle.entry_time.strftime('%Y-%m-%d %H:%M:%S')}.")

    def unpark_vehicle(self):
        license_plate = input("Enter vehicle license plate to unpark: ").strip()
        slot = None
        for s in self.slots:
            if s.is_occupied and s.vehicle.license_plate == license_plate:
                slot = s
                break
        if not slot:
            print("Vehicle not found in parking.")
            return

        parked_vehicle = slot.unpark()
        exit_time = datetime.now()
        parked_duration = exit_time - parked_vehicle.entry_time
        hours = parked_duration.total_seconds() / 3600
        fee = self.calculate_fee(parked_vehicle.get_type(), hours)

        save_data(self.slots)
        log_activity(f"Vehicle {license_plate} unparked from slot {slot.slot_id}. Duration: {hours:.2f} hours. Fee: ₹{fee}")

        print(f"Vehicle {license_plate} unparked from slot {slot.slot_id}.")
        print(f"Parked duration: {hours:.2f} hours")
        print(f"Parking fee: ₹{fee}")

    def calculate_fee(self, vehicle_type, hours):
        rates = {'car': 20, 'bike': 10}  # ₹20/hr for cars, ₹10/hr for bikes
        min_fee = {'car': 20, 'bike': 10}
        fee = int(hours * rates[vehicle_type])
        return fee if fee >= min_fee[vehicle_type] else min_fee[vehicle_type]

    def view_available_slots(self):
        print("\nAvailable Slots:")
        for vtype in ['car', 'bike']:
            free_slots = [s.slot_id for s in self.slots if s.slot_type == vtype and not s.is_occupied]
            print(f"{vtype.title()} slots free: {len(free_slots)} - {', '.join(free_slots) if free_slots else 'None'}")

    def view_parked_vehicles(self):
        print("\nParked Vehicles:")
        occupied_slots = [s for s in self.slots if s.is_occupied]
        if not occupied_slots:
            print("No vehicles parked currently.")
            return
        for slot in occupied_slots:
            v = slot.vehicle
            print(f"Slot {slot.slot_id}: {v.get_type().title()} {v.license_plate} (Parked at {v.entry_time.strftime('%Y-%m-%d %H:%M:%S')})")

    def search_vehicle(self):
        query = input("Enter license plate to search: ").strip()
        found_slots = [s for s in self.slots if s.is_occupied and query in s.vehicle.license_plate]
        if not found_slots:
            print("No matching vehicle found.")
            return
        for slot in found_slots:
            v = slot.vehicle
            print(f"Found: Slot {slot.slot_id}, {v.get_type().title()} {v.license_plate}, Parked at {v.entry_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def admin_panel(self):
        print("\n--- Admin Panel ---")
        print("1. View All Slots")
        print("2. View Log File")
        print("3. Reset Parking Data")
        print("0. Exit Admin Panel")

        choice = input("Enter choice: ")
        if choice == '1':
            self.view_all_slots()
        elif choice == '2':
            self.view_logs()
        elif choice == '3':
            self.reset_data()
        elif choice == '0':
            print("Exiting Admin Panel.")
        else:
            print("Invalid choice.")

    def view_all_slots(self):
        print("\nAll Slots Status:")
        for slot in self.slots:
            status = "Occupied" if slot.is_occupied else "Free"
            vehicle_info = f"{slot.vehicle.get_type().title()} {slot.vehicle.license_plate}" if slot.is_occupied else "None"
            print(f"Slot {slot.slot_id} [{slot.slot_type.title()}] - {status} - Vehicle: {vehicle_info}")

    def view_logs(self):
        print("\nActivity Log:")
        try:
            with open('activity.log', 'r') as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("No logs found.")

    def reset_data(self):
        confirm = input("Are you sure you want to reset all parking data? (yes/no): ")
        if confirm.lower() == 'yes':
            for slot in self.slots:
                slot.is_occupied = False
                slot.vehicle = None
            save_data(self.slots)
            log_activity("All parking data reset by admin.")
            print("Parking data has been reset.")
        else:
            print("Reset cancelled.")
