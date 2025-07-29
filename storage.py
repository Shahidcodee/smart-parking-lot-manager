import json
from vehicle import Car, Bike
from slot import ParkingSlot
from datetime import datetime

DATA_FILE = 'parking_data.json'

def save_data(slots):
    data = []
    for slot in slots:
        d = {
            'slot_id': slot.slot_id,
            'slot_type': slot.slot_type,
            'is_occupied': slot.is_occupied,
            'vehicle': None
        }
        if slot.vehicle:
            d['vehicle'] = {
                'license_plate': slot.vehicle.license_plate,
                'vehicle_type': slot.vehicle.get_type(),
                'entry_time': slot.vehicle.entry_time.strftime('%Y-%m-%d %H:%M:%S')
            }
        data.append(d)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def load_data():
    slots = []
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            for d in data:
                slot = ParkingSlot(d['slot_id'], d['slot_type'])
                slot.is_occupied = d['is_occupied']
                if d['vehicle']:
                    vtype = d['vehicle']['vehicle_type']
                    if vtype == 'car':
                        vehicle = Car(d['vehicle']['license_plate'])
                    else:
                        vehicle = Bike(d['vehicle']['license_plate'])
                    vehicle.entry_time = datetime.strptime(d['vehicle']['entry_time'], '%Y-%m-%d %H:%M:%S')
                    slot.vehicle = vehicle
                slots.append(slot)
    except FileNotFoundError:
        pass  # No data file yet
    return slots
