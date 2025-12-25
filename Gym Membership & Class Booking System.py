# Members list
members = []

# Trainer information
trainers = [
    {"trainer_id": 1, "name": "Hari", "specialization": "Yoga"},
    {"trainer_id": 2, "name": "Sita", "specialization": "Cardio"}
]

# Classes information
classes = [
    {"class_id": 1, "name": "Yoga Morning", "time": "6AM-7AM", "trainer_id": 1, "max_capacity": 5, "booked_members": []},
    {"class_id": 2, "name": "Cardio Evening", "time": "6PM-7PM", "trainer_id": 2, "max_capacity": 5, "booked_members": []}
]

# Auto-increment member ID
next_member_id = 1

# Let's register a member here
def register_member():
    global next_member_id
    print("\n=== Member Registration ===")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    membership_type = input("Enter membership type (basic/premium): ")

    member = {
        "member_id": next_member_id,
        "name": name,
        "phone": phone,
        "membership_type": membership_type
    }

    members.append(member)
    print(f"Registration successful! Your Member ID is {next_member_id}")

    next_member_id += 1

# Let's see the available classes
def view_classes():
    print("\n=== Available Classes ===")
    for cls in classes:
        trainer_name = next(t["name"] for t in trainers if t["trainer_id"] == cls["trainer_id"])
        slots_left = cls["max_capacity"] - len(cls["booked_members"])
        print(f"Class ID: {cls['class_id']}, Name: {cls['name']}, Time: {cls['time']}, Trainer: {trainer_name}, Slots Left: {slots_left}")

# Let's book a class now
def book_class():
    if not members:
        print("No members registered yet. Please register first.")
        return
    
    try:
        member_id = int(input("Enter your Member ID: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("Member ID not found. Please register first.")
        return
    
    view_classes()
    
    try:
        class_id = int(input("Enter the Class ID you want to book: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    cls = next((c for c in classes if c["class_id"] == class_id), None)
    if not cls:
        print("Class ID not found.")
        return
    
    if member_id in cls["booked_members"]:
        print("You have already booked this class.")
        return
    
    if len(cls["booked_members"]) >= cls["max_capacity"]:
        print("Class is full! Cannot book.")
        return
    
    cls["booked_members"].append(member_id)
    print(f"Booking successful! {member['name']} booked {cls['name']} at {cls['time']}")

# Let's make the traineer view
def trainer_view():
    try:
        trainer_id = int(input("Enter Trainer ID: "))
    except ValueError:
        print("Invalid input!")
        return
    
    trainer = next((t for t in trainers if t["trainer_id"] == trainer_id), None)
    if not trainer:
        print("Trainer not found.")
        return
    
    print(f"\n=== Classes for Trainer: {trainer['name']} ===")
    trainer_classes = [c for c in classes if c["trainer_id"] == trainer_id]
    
    if not trainer_classes:
        print("No classes assigned.")
        return
    
    for cls in trainer_classes:
        print(f"\nClass: {cls['name']}, Time: {cls['time']}")
        if cls["booked_members"]:
            print("Booked Members:")
            for m_id in cls["booked_members"]:
                member = next((m for m in members if m["member_id"] == m_id), None)
                print(f"- {member['name']} (ID: {member['member_id']}, Phone: {member['phone']})")
        else:
            print("No members booked yet.")


# Now make main menu
def main_menu():
    while True:
        print("\n=== Gym Membership & Class Booking System ===")
        print("1. Register Member")
        print("2. View Available Classes")
        print("3. Book a Class")
        print("4. Trainer View")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_member()
        elif choice == "2":
            view_classes()
        elif choice == "3":
            book_class()
        elif choice == "4":
            trainer_view()
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")



if __name__ == "__main__":
    main_menu()




    