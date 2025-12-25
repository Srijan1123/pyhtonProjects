from datetime import datetime

#  Define doctors first
doctors = [
    {
        "id": 1,
        "name": "Dr. srijan basnet",
        "specialization": "Cardiologist",
        "available_time": "10:00 AM - 2:00 PM",
        "max_patients": 5,
        "appointments": []
    },
    {
        "id": 2,
        "name": "Dr. ankit karn",
        "specialization": "Orthopedic",
        "available_time": "12:00 PM - 4:00 PM",
        "max_patients": 5,
        "appointments": []
    },
    {
        "id": 3,
        "name": "Dr. ayush",
        "specialization": "Dermatologist",
        "available_time": "2:00 PM - 6:00 PM",
        "max_patients": 5,
        "appointments": []
    },

    {
        "id": 3,
        "name": "Dr. suraj panthi",
        "specialization": "Dermatologist",
        "available_time": "2:00 PM - 6:00 PM",
        "max_patients": 5,
        "appointments": []
    }
]

# show the Facilities
facilities = ["Free WiFi", "AC Waiting Room", "24/7 Pharmacy"]

# let Display doctors
def display_doctors():
    print("\n--- Available Doctors ---")
    for doc in doctors:
        print(f"{doc['id']}. {doc['name']} | {doc['specialization']} | Time: {doc['available_time']} | Slots left: {doc['max_patients'] - len(doc['appointments'])}")

# now let's Book the appointment
def book_appointment():
    display_doctors()
    try:
        doctor_choice = int(input("Select doctor by ID: "))
        doctor = next(d for d in doctors if d["id"] == doctor_choice)
    except (ValueError, StopIteration):
        print("Invalid doctor selection!")
        return

    if len(doctor["appointments"]) >= doctor["max_patients"]:
        print("❌ Doctor's appointment slots are full!")
        return

    name = input("Enter patient name: ")
    phone = input("Enter phone number: ")
    date_str = input("Enter appointment date (YYYY-MM-DD): ")

    try:
        appointment_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format!")
        return

    # Add appointment
    appointment = {
        "name": name,
        "phone": phone,
        "date": appointment_date
    }
    doctor["appointments"].append(appointment)
    print(f"\n✅ Appointment booked for {name} with {doctor['name']} on {appointment_date}.")
    print(f"Facilities available: {', '.join(facilities)}")

    # now let's  Show all appointments
def show_appointments():
    print("\n--- Appointment Details ---")
    for doc in doctors:
        print(f"\nDoctor: {doc['name']} ({doc['specialization']}) | Time: {doc['available_time']}")
        if doc["appointments"]:
            for appt in doc["appointments"]:
                print(f"  Patient: {appt['name']} | Phone: {appt['phone']} | Date: {appt['date']}")
        else:
            print("  No bookings yet.")

# now let's show the  Main menu
def main():
    while True:
        print("\n🏥 Hospital Appointment System 🏥")
        print("1. Book Appointment")
        print("2. Show Doctors")
        print("3. Show Appointments")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_appointment()
        elif choice == "2":
            display_doctors()
        elif choice == "3":
            show_appointments()
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")


main()
