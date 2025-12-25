bookings = []
next_id = 1

# Available movies, showtimes, and seat categories
movies = ["Inception", "Interstellar", "Avengers", "Joker"]
show_times = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM"]
seat_categories = {
    "VIP": 500,
    "Regular": 300,
    "Balcony": 200
}

# 🪑 Book movie ticket
def book_ticket():
    global next_id
    print("\n --- Book Movie Ticket ---")

    print("\nAvailable Movies:")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie}")
    try:
        movie_choice = int(input("Select movie (1-4): "))
        movie_name = movies[movie_choice - 1]
    except (ValueError, IndexError):
        print("Invalid movie selection!")
        return

    date = input("Enter show date (YYYY-MM-DD): ").strip()

    print("\nAvailable Show Times:")
    for i, st in enumerate(show_times, 1):
        print(f"{i}. {st}")
    try:
        time_choice = int(input("Select show time (1-4): "))
        show_time = show_times[time_choice - 1]
    except (ValueError, IndexError):
        print("Invalid show time!")
        return

    print("\nSeat Categories:")
    for i, (cat, price) in enumerate(seat_categories.items(), 1):
        print(f"{i}. {cat} - Rs.{price}")
    try:
        cat_choice = int(input("Select seat category (1-3): "))
        seat_category = list(seat_categories.keys())[cat_choice - 1]
    except (ValueError, IndexError):
        print("Invalid seat category!")
        return

    seat_no = input("Enter seat number (e.g., A1, B2): ").strip().upper()

    # Check if seat already booked
    for b in bookings:
        if b["movie"] == movie_name and b["date"] == date and b["seat_no"] == seat_no:
            print("❌ This seat is already booked for this show!")
            return

    booking = {
        "id": next_id,
        "movie": movie_name,
        "date": date,
        "show_time": show_time,
        "seat_no": seat_no,
        "category": seat_category,
        "price": seat_categories[seat_category],
        "status": "Confirmed"
    }

    bookings.append(booking)
    print(f"\n Booking Confirmed for {movie_name} on {date} at {show_time}")
    print(f"Seat: {seat_no} ({seat_category}) | Price: Rs.{seat_categories[seat_category]}")
    next_id += 1


#  View all bookings
def view_bookings():
    if not bookings:
        print("\nNo bookings found!")
        return
    print("\n--- All Bookings ---")
    print(f"{'ID':<5} {'Movie':<15} {'Date':<12} {'Time':<10} {'Seat':<8} {'Category':<10} {'Price':<8} {'Status':<10}")
    print("-" * 80)
    for b in bookings:
        print(f"{b['id']:<5} {b['movie']:<15} {b['date']:<12} {b['show_time']:<10} {b['seat_no']:<8} {b['category']:<10} Rs.{b['price']:<8} {b['status']:<10}")


#  Cancel booking
def cancel_booking():
    try:
        bid = int(input("\nEnter Booking ID to cancel: "))
    except ValueError:
        print("Invalid input!")
        return

    for b in bookings:
        if b["id"] == bid:
            if b["status"] == "Cancelled":
                print(" This booking is already cancelled!")
                return
            b["status"] = "Cancelled"
            print(f" Booking ID {bid} cancelled successfully!")
            return

    print("Booking not found!")


# Filter bookings by date
def filter_by_date():
    date = input("\nEnter date to filter (YYYY-MM-DD): ").strip()
    filtered = [b for b in bookings if b["date"] == date]
    if not filtered:
        print("No bookings found for this date!")
        return
    print(f"\n Bookings for {date}:")
    for b in filtered:
        print(f"ID: {b['id']} | Movie: {b['movie']} | Seat: {b['seat_no']} | Status: {b['status']}")


# Main menu
def main_menu():
    while True:
        print("\n=======  Movie Ticket Booking System =======")
        print("1. Book Ticket")
        print("2. View All Bookings")
        print("3. Cancel Booking")
        print("4. Filter Bookings by Date")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            filter_by_date()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main_menu()
