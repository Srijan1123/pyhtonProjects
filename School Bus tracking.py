import datetime

buses = []
students = []
bus_logs = []


def add_bus():
    print("\n=== Add Buses Here ===")
    bus_number = input("Enter bus number: ").strip().upper()
    driver_name = input("Enter driver name: ").strip().title()
    route_name = input("Enter route name: ").strip().title()
    seats = input("Enter total seats: ").strip()
    contact = input("Enter driver contact number: ").strip()

    buses.append({
        "bus_number": bus_number,
        "driver": driver_name,
        "route": route_name,
        "contact": contact,
        "seats": seats,
        "status": "Not Started"
    })

    print(f"Bus {bus_number} added successfully!\n")


def assign_student():
    print("\n=== Assign Student ===")
    name = input("Enter student name: ").strip().title()
    roll = input("Enter roll number: ").strip()
    class_name = input("Enter class name: ").strip()
    stop_name = input("Enter stop name: ").strip().title()
    bus_number = input("Enter assigned bus number: ").strip().upper()

    for bus in buses:
        if bus['bus_number'] == bus_number:
            students.append({
                "name": name,
                "roll": roll,
                "class": class_name,
                "stop": stop_name,
                "bus": bus_number
            })
            print(f"Student {name} assigned to Bus {bus_number}\n")
            return

    print("Bus not found! Please add the bus first.\n")


def update_bus():
    print("\n=== Update Bus Status ===")
    bus_number = input("Enter bus number: ").strip().upper()
    status = input("Enter status (Not Started / On Route / Reached School / Reached Home): ").strip().title()

    for bus in buses:
        if bus['bus_number'] == bus_number:
            bus['status'] = status
            time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            bus_logs.append({
                "bus_number": bus_number,
                "status": status,
                "time": time_now
            })

            print(f"Status updated for Bus {bus_number} → {status}")
            simulate_parent_alert(bus_number, status)
            return

    print("❌ Bus not found!\n")


def simulate_parent_alert(bus_number, status):
    print(f"📢 Parent Alert: Bus {bus_number} is now '{status}'. Please take necessary action.\n")


def view_buses():
    if not buses:
        print("No buses added yet!\n")
        return

    print("\n=== All Buses ===")
    print(f"{'Bus No':<10}{'Driver':<15}{'Route':<15}{'Seats':<8}{'Status':<15}")
    print("-" * 65)
    for bus in buses:
        print(f"{bus['bus_number']:<10}{bus['driver']:<15}{bus['route']:<15}{bus['seats']:<8}{bus['status']:<15}")
    print()


def view_students():
    if not students:
        print("No students assigned yet!\n")
        return

    print("\n=== Assigned Students ===")
    print(f"{'Name':<15}{'Roll':<10}{'Class':<10}{'Stop':<15}{'Bus':<10}")
    print("-" * 60)
    for s in students:
        print(f"{s['name']:<15}{s['roll']:<10}{s['class']:<10}{s['stop']:<15}{s['bus']:<10}")
    print()


def view_logs():
    if not bus_logs:
        print("No bus logs recorded yet!\n")
        return

    print("\n=== View Logs ===")
    print(f"{'Bus No':<10}{'Status':<20}{'Time'}")
    print("-" * 60)
    for log in bus_logs:
        print(f"{log['bus_number']:<10}{log['status']:<20}{log['time']}")
    print()


def main_menu():
    while True:
        print("\n==== MAIN MENU ====")
        print("1. Add New Bus")
        print("2. Assign Student to Bus")
        print("3. Update Bus Status")
        print("4. View All Buses")
        print("5. View Assigned Students")
        print("6. View Daily Logs")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_bus()
        elif choice == "2":
            assign_student()
        elif choice == "3":
            update_bus()
        elif choice == "4":
            view_buses()
        elif choice == "5":
            view_students()
        elif choice == "6":
            view_logs()
        elif choice == "7":
            print("Exiting system... Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main_menu()
