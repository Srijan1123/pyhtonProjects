# adding rooms, booking, availability check, and checkout.
rooms = []
bookings = []
next_id = 1

# let's add the room
def add_room():
    global next_id
    print("\n--- ADD ROOMS ---")
    room_number = input("Enter room number: ").strip()
    room_type = input("Enter room type (single/double/suite): ").strip()
    price = input("Enter room price per night: ").strip()
    
    room = {
        "id": next_id,
        "room_number": room_number,
        "room_type": room_type,
        "price": int(price),
        "available": True
    }
    rooms.append(room)
    print(f"Room {room_number} added successfully!..")
    next_id += 1

# Let's book a room
def book_room():
    if not rooms:
        print("No room available as of now...")
        return
    room_number = input("Enter a room number to book: ").strip()
    for room in rooms:
        if room['room_number'] == room_number and room['available']:
            name = input("Enter your name: ").strip()
            days = int(input("Enter number of days: ").strip())
            
            booking = {
                "room_number": room_number,
                "customer": name,
                "days": days,
                "total_cost": room['price'] * days
            }
            
            bookings.append(booking)
            room["available"] = False
            print(f"Room {room_number} has been booked for {name} successfully!!..")
            return
    print("Room not available or does not exist..")

# Now let's see all of the bookings
def view_bookings():
    if not bookings:
        print("No room has been booked yet...")
        return
    print("\n--- All Bookings ---")
    print(f"{'Room':<10} {'Customer':15} {'Days':<5} {'Total Cost'}")
    print("-" * 60)
    for b in bookings:
        print(f"{b['room_number']:<10} {b['customer']:15} {b['days']:<5} {b['total_cost']}")
    print("-" * 60)

# Now let's check out the room
def check_out():
    room_number = input("Enter room number to checkout: ").strip()
    for booking in bookings:
        if booking["room_number"] == room_number:
            bookings.remove(booking)
            for room in rooms:
                if room["room_number"] == room_number:
                    room["available"] = True
            print(f"Room {room_number} has been checked out...")
            return
    print("No bookings found for this room...")

# let's make the main menu
def main_menu():
    while True:
        print("\n----- Hotel Booking System -----")
        print("1. Add room")
        print("2. Book room")
        print("3. View bookings")
        print("4. Checkout room")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_room()
        elif choice == "2":
            book_room()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            check_out()
        elif choice == "5":
            print("Exiting the system..")
            break
        else:
            print("Invalid choice. Try again...")

if __name__ == "__main__":
    main_menu()
