from datetime import datetime

# let's Define bus routes and info
buses = [
    {
        "bus_name": "Mountain Express",
        "route": "Kathmandu to Pokhara",
        "leaving_time": "07:00 AM",
        "stops": ["Dhulikhel", "Banepa", "Kurintar"],
        "facilities": ["Free Internet", "TV"],
        "price_per_passenger": 1200,
        "bookings": []  # store bookings
    },
    {
        "bus_name": "Himalayan Travels",
        "route": "Kathmandu to Kakarvitta",
        "leaving_time": "06:30 AM",
        "stops": ["Dhulikhel", "Banepa", "Biratnagar"],
        "facilities": ["Free Internet", "TV"],
        "price_per_passenger": 1500,
        "bookings": []
    },
    {
        "bus_name": "Everest Line",
        "route": "Kathmandu to Itahari",
        "leaving_time": "08:00 AM",
        "stops": ["Dhulikhel", "Banepa", "Bharatpur"],
        "facilities": ["Free Internet", "TV"],
        "price_per_passenger": 1300,
        "bookings": []
    }
]

# elt's create a function to display buses
def display_buses():
    print("\n--- Available Buses ---")
    for i, bus in enumerate(buses, 1):
        print(f"{i}. {bus['bus_name']} | Route: {bus['route']} | Departure: {bus['leaving_time']} | Price: Rs.{bus['price_per_passenger']}")
        print(f"    Stops: {', '.join(bus['stops'])}")
        print(f"    Facilities: {', '.join(bus['facilities'])}")
        print(f"    Bookings: {len(bus['bookings'])} passengers\n")

# now let's make Booking function
def book_bus():
    display_buses()
    try:
        bus_choice = int(input("Select bus by number: "))
        bus = buses[bus_choice - 1]
    except (ValueError, IndexError):
        print("Invalid bus selection!")
        return

    name = input("Enter passenger name: ")
    phone = input("Enter phone number: ")
    date_str = input("Enter departure date (YYYY-MM-DD): ")

    # now let's work on Validate date
    try:
        departure_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format!")
        return

    try:
        num_passengers = int(input("Enter number of passengers: "))
        if num_passengers <= 0:
            print("Number of passengers must be positive!")
            return
    except ValueError:
        print("Invalid input for number of passengers!")
        return

    # now let's work on Record booking
    booking_info = {
        "name": name,
        "phone": phone,
        "departure_date": departure_date,
        "num_passengers": num_passengers
    }
    bus["bookings"].append(booking_info)
    total_price = bus["price_per_passenger"] * num_passengers
    print(f"\n✅ Booking confirmed for {name} ({num_passengers} passengers). Total price: Rs.{total_price}")

# let's work on Show bookings
def show_bookings():
    print("\n--- All Bus Bookings ---")
    for bus in buses:
        print(f"\nBus: {bus['bus_name']} | Route: {bus['route']} | Departure: {bus['leaving_time']}")
        if bus["bookings"]:
            for b in bus["bookings"]:
                print(f"  Passenger: {b['name']}, Phone: {b['phone']}, Date: {b['departure_date']}, Seats: {b['num_passengers']}")
        else:
            print("  No bookings yet.")

# now make Main menu
def main():
    while True:
        print("\n🚌 Bus Booking System 🚌")
        print("1. Book a Bus")
        print("2. Show Available Buses")
        print("3. Show All Bookings")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_bus()
        elif choice == "2":
            display_buses()
        elif choice == "3":
            show_bookings()
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")


main()
