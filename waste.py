import datetime

users = []
waste_submissions = []
pickups = []

def add_user():
    print("\n --- Add User ---")
    name = input("Enter your name: ").strip().title()
    address = input("Enter your address: ").strip().title()
    contact = input("Enter contact number here: ").strip()
    
    user = {
        "name": name,
        "address": address,
        "contact": contact,
        "points": 0
    }
    
    users.append(user)
    print(f"User {name} added successfully!...")

def submit_waste():
    print("\n --- Waste Submission ---")
    if not users:
        print("No user found. Add user first...")
        return
    
    name = input("Enter your name: ").strip().title()
    user = next((u for u in users if u['name'] == name), None)
    
    if not user:
        print("User not found!...") 
        return
    
    waste_type = input("Enter waste type (plastic/metal/organic/paper): ").strip().lower()
    weight = float(input("Enter weight (in kg): ").strip())
    
    point_per_kg = {
        "plastic": 5,
        "metal": 10,
        "organic": 15,
        "paper": 2
    }
    
    points = point_per_kg.get(waste_type, 1) * weight
    user['points'] += points
    
    waste = {
        "user": name,
        "type": waste_type,
        "points": points,
        "date": datetime.date.today()
    }
    
    waste_submissions.append(waste)
    print(f"{waste_type} waste of {weight}kg submitted. You earn {points} points!")

def request_pickup():
    print("\n--- Request Pickup ---")
    name = input("Enter your name: ").strip().title()
    address = input("Input your address here: ").strip().title()
    date = input("Enter preferred date (yyyy-mm-dd): ").strip()
    
    pickup_request = {
        "name": name,
        "address": address,
        "date": date,
        "status": 'pending'
    }
    
    pickups.append(pickup_request)
    print(f"Pickup requested for {name} on {date}. Status: pending")

def view_user_report():
    print("\n --- User Report ---")
    if not users:
        print("No user found...")
        return
    
    for u in users:
        print(f"{u['name']} | Address: {u['address']} | Points: {u['points']}")

def view_system_summary():
    print("\n --- System Summary ---")
    print(f"Total users: {len(users)}")
    print(f"Total waste submissions: {len(waste_submissions)}")
    print(f"Total pickups requested: {len(pickups)}")
    
    total_points = sum(u['points'] for u in users)
    print(f"Total reward points distributed: {total_points}")

def main_menu():
    while True:
        print("\n === Main Menu ===")
        print("1. Add user")
        print("2. Submit waste")
        print("3. Request pickup")
        print("4. View user report")
        print("5. View system summary")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_user()
            
        elif choice == "2":
            submit_waste()
            
        elif choice == "3":
            request_pickup()
            
        elif choice == "4":
            view_user_report()
            
        elif choice == "5":
            view_system_summary()
            
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again...")

if __name__ == "__main__":
    main_menu()
