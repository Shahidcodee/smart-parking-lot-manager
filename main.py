from manager import ParkingLotManager
from auth import authenticate_admin
from utils import clear_screen

def main():
    manager = ParkingLotManager()
    while True:
        clear_screen()
        print("""
===== SMART PARKING LOT MANAGER =====
1. Park Vehicle
2. Unpark Vehicle
3. View Available Slots
4. View Parked Vehicles
5. Search Vehicle
6. Admin Panel
0. Exit
        """)
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            manager.park_vehicle()
        elif choice == '2':
            manager.unpark_vehicle()
        elif choice == '3':
            manager.view_available_slots()
        elif choice == '4':
            manager.view_parked_vehicles()
        elif choice == '5':
            manager.search_vehicle()
        elif choice == '6':
            if authenticate_admin():
                while True:
                    manager.admin_panel()
                    if input("\nReturn to admin panel? (y/n): ").lower() != 'y':
                        break
        elif choice == '0':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
