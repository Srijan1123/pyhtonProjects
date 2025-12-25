
from datetime import datetime

# List of tables
tables = [
    {"table_id": 1, "capacity": 2},
    {"table_id": 2, "capacity": 4},
    {"table_id": 3, "capacity": 6},
    {"table_id": 4, "capacity": 8},
    {"table_id": 5, "capacity": 2},
    {"table_id": 6, "capacity": 7},
    {"table_id": 7, "capacity": 10},
    {"table_id": 8, "capacity": 8}
]

reservations = []

next_reservation_id = 1

# let's check the available table
def is_table_available(table_id, date, start_time, end_time):
    for res in reservations:
        if res["table_id"] == table_id and res["reservation_date"] == date:
            # Check for time overlap
            if not (end_time <= res["start_time"] or start_time >= res["end_time"]):
                return False
    return True


# let's View Available Tables
def view_available_tables():
    date = input("Enter reservation date (YYYY-MM-DD): ")
    start_time = input("Enter start time (HH:MM in 24hr format): ")
    end_time = input("Enter end time (HH:MM in 24hr format): ")

    print("\n=== Available Tables ===")
    available = False
    for table in tables:
        if is_table_available(table["table_id"], date, start_time, end_time):
            print(f"Table {table['table_id']} - Capacity: {table['capacity']}")
            available = True
    if not available:
        print("No tables available for the given time slot.")


# let's Book a Table
def book_table():
    global next_reservation_id

    customer_name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    try:
        number_of_people = int(input("Enter number of people: "))
    except ValueError:
        print("Invalid number of people!")
        return

    reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
    start_time = input("Enter start time (HH:MM in 24hr format): ")
    end_time = input("Enter end time (HH:MM in 24hr format): ")

    # let's choose a table
    for table in tables:
        if table["capacity"] >= number_of_people and is_table_available(table["table_id"], reservation_date, start_time, end_time):
            reservation = {
                "reservation_id": next_reservation_id,
                "customer_name": customer_name,
                "phone_number": phone_number,
                "number_of_people": number_of_people,
                "reservation_date": reservation_date,
                "start_time": start_time,
                "end_time": end_time,
                "table_id": table["table_id"]
            }
            reservations.append(reservation)
            print(f"\n✅ Reservation successful! Your Reservation ID is {next_reservation_id}, Table {table['table_id']} reserved.")
            next_reservation_id += 1
            return

    print("\nNo suitable table available for the given time slot.")

#let's see all of our reservation
def view_reservations():
    if not reservations:
        print("\nNo reservations found.")
        return

    print("\n=== All Reservations ===")
    for res in reservations:
        print(f"ID: {res['reservation_id']}, Name: {res['customer_name']}, Phone: {res['phone_number']}, "
              f"People: {res['number_of_people']}, Date: {res['reservation_date']}, "
              f"Time: {res['start_time']} - {res['end_time']}, Table: {res['table_id']}")

#let's make a main menu 
def main_menu():
    while True:
        print("\n=== Restaurant Reservation System ===")
        print("1. View Available Tables")
        print("2. Book a Table")
        print("3. View Reservations")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_available_tables()
        elif choice == "2":
            book_table()
        elif choice == "3":
            view_reservations()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
