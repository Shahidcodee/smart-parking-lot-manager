# main.py

from parking_lot import ParkingLot

def main():
    parking_lot = ParkingLot()

    while True:
        print("\n========== SMART PARKING LOT ==========")
        print("1. Park Vehicle")
        print("2. Unpark Vehicle")
        print("3. Show Available Slots")
        print("4. Search Vehicle")
        print("5. Exit")
        print("=======================================")

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            number = input("Enter vehicle number: ").strip()
            print("Choose vehicle type: compact / suv / two_wheeler")
            vtype = input("Enter vehicle type: ").strip().lower()
            if vtype not in ['compact', 'suv', 'two_wheeler']:
                print("❌ Invalid vehicle type.")
            else:
                parking_lot.park_vehicle(number, vtype)

        elif choice == '2':
            number = input("Enter vehicle number to unpark: ").strip()
            parking_lot.unpark_vehicle(number)

        elif choice == '3':
            parking_lot.show_available_slots()

        elif choice == '4':
            number = input("Enter vehicle number to search: ").strip()
            parking_lot.search_vehicle(number)

        elif choice == '5':
            print("👋 Thank you for using Smart Parking Lot.")
            break

        else:
            print("❌ Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()
