print("\n---Simple futsal booking system---")
  #opening and closing time
OPENING_TIME = 6   # 6 AM
CLOSING_TIME = 20  # 8 PM
PRICE_PER_HOUR = 120

# let's  Create time slots (6 AM - 8 PM)
time_slots = {hour: None for hour in range(OPENING_TIME, CLOSING_TIME)}  # None = available

# let's create a Function to display available slots
def display_slots():
    print("\n--- Futsal Time Slots ---")
    for hour, booking in time_slots.items():
        slot_time = f"{hour}:00 - {hour+1}:00"
        if booking is None:
            print(f"{slot_time} → Available")
        else:
            print(f"{slot_time} → Booked by {booking['name']} ({booking['phone']})")

# now Booking function
def book_slot():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    try:
        hours = int(input("Enter number of hours (1 or 2, more = full day): "))
    except ValueError:
        print("Invalid input!")
        return

    if hours > 2:
        print("\n⚽ Full day booking selected!")
        for hour in range(OPENING_TIME, CLOSING_TIME):
            time_slots[hour] = {"name": name, "phone": phone}
        cost = (CLOSING_TIME - OPENING_TIME) * PRICE_PER_HOUR
        print(f"Booking confirmed for full day. Total cost: Rs.{cost}")
        return

    start_time = int(input(f"Enter start time (between {OPENING_TIME} and {CLOSING_TIME-1}): "))

    # now check the validation
    if start_time < OPENING_TIME or start_time + hours > CLOSING_TIME:
        print("Invalid time selection!")
        return

    # now let's Check the availability
    for hour in range(start_time, start_time + hours):
        if time_slots[hour] is not None:
            print("❌ Selected slot is already booked!")
            return

    # let's Book the slots
    for hour in range(start_time, start_time + hours):
        time_slots[hour] = {"name": name, "phone": phone}

    cost = hours * PRICE_PER_HOUR
    print(f"✅ Booking confirmed for {hours} hour(s). Total cost: Rs.{cost}")

# Owner view 
def owner_view():
    print("\n--- Owner Booking Overview ---")
    display_slots()

# our Main menu
def main():
    while True:
        print("\n⚽ Futsal Booking System ⚽")
        print("1. Book Futsal")
        print("2. View Available Slots")
        print("3. Owner View (all bookings)")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_slot()
        elif choice == "2":
            display_slots()
        elif choice == "3":
            owner_view()
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")


main()
