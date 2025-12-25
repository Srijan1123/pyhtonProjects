from datetime import datetime

parking_lot = {}

# Let's add vehicle first
def add_vehicle():
    print("\n---- Add Vehicle ----")
    vehicle_no = input("Enter vehicle number (BA-2-PA-1234): ").strip().upper()
    slot = input("Enter parking slot number (S1, S2, S3): ").strip().upper()
    
    if slot in parking_lot:
        print(f"Slot {slot} is already occupied by {parking_lot[slot]['vehicle']}.\n")
        return
    
    for info in parking_lot.values():
        if info['vehicle'] == vehicle_no:
            print("This vehicle is already parked...\n")
            return

    entry_time = datetime.now()
    parking_lot[slot] = {'vehicle': vehicle_no, 'entry': entry_time}
    print(f"✅ Vehicle {vehicle_no} parked successfully at slot {slot} at {entry_time.strftime('%H:%M:%S')}.\n")

# Let's view the parking status
def view_status():
    print("\n---- Parking Status ----")
    if not parking_lot:
        print("No vehicles have been parked yet...\n")
        return
    
    print(f"{'Slot':<10}{'Vehicle Number':<20}{'Entry Time':<20}")
    print("-" * 50)
    
    for slot, info in parking_lot.items():
        print(f"{slot:<10}{info['vehicle']:<20}{info['entry'].strftime('%H:%M:%S'):<20}")
    print()

# Let's calculate vehicle fee and exit
def vehicle_exit():
    print("\n---- Vehicle Exit ----")
    slot = input("Enter slot number to free: ").strip().upper()
    
    if slot not in parking_lot:
        print("❌ Invalid slot number or no vehicle found.\n")
        return
    
    exit_time = datetime.now()
    entry_time = parking_lot[slot]['entry']
    vehicle_no = parking_lot[slot]['vehicle']
    
    duration = (exit_time - entry_time).total_seconds() / 60  # in minutes
    rate_per_min = 2
    total_fee = duration * rate_per_min
    
    print(f"\nVehicle: {vehicle_no}")
    print(f"Entry Time: {entry_time.strftime('%H:%M:%S')}")
    print(f"Exit Time: {exit_time.strftime('%H:%M:%S')}")
    print(f"Total Duration: {duration:.2f} minutes")
    print(f"Total Fee: Rs. {total_fee:.2f}\n")
    
    del parking_lot[slot]
    print(f"✅ Slot {slot} is now free.\n")

# Let's make the main menu here
def main_menu():
    while True:
        print("\n===== Main Menu =====")
        print("1. Add Vehicle")
        print("2. View Parking Status")
        print("3. Vehicle Exit & Fee Calculation")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_vehicle()
        elif choice == "2":
            view_status()
        elif choice == "3":
            vehicle_exit()
        elif choice == "4":
            print("Exiting System... Goodbye!\n")
            break
        else:
            print("Invalid choice. Try again!\n")

if __name__ == "__main__":
    main_menu()
