medicines = []  # List to store all medicines
next_medicine_id = 1  # Auto-increment medicine ID

# Function: Add Medicine
def add_medicine():
    """Add new medicine to the pharmacy."""
    global next_medicine_id
    print("\n=== Add New Medicine ===")
    name = input("Enter medicine name: ")
    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input! Price must be number, quantity must be integer.")
        return
    expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
    
    medicine = {
        "medicine_id": next_medicine_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "expiry_date": expiry_date
    }
    
    medicines.append(medicine)
    print(f"Medicine '{name}' added successfully with ID {next_medicine_id}!")
    next_medicine_id += 1

# Function to view medicine
def view_medicines():
    """Show all available medicines with stock and expiry."""
    print("\n=== Available Medicines ===")
    if not medicines:
        print("No medicines available.")
        return
    for med in medicines:
        print(f"ID: {med['medicine_id']}, Name: {med['name']}, Price: Rs.{med['price']}, Quantity: {med['quantity']}, Expiry: {med['expiry_date']}")

# Function to sell medicine
def sell_medicine():
    """Sell medicine to customer, update stock, and generate bill."""
    if not medicines:
        print("No medicines available to sell.")
        return
    
    customer_name = input("Enter customer name: ")
    customer_phone = input("Enter customer phone: ")
    
    cart = []  # List to store purchased items
    total_amount = 0
    
    while True:
        view_medicines()
        try:
            med_id = int(input("Enter Medicine ID to buy (0 to finish): "))
        except ValueError:
            print("Invalid input!")
            continue
        
        if med_id == 0:
            break
        
        medicine = next((m for m in medicines if m["medicine_id"] == med_id), None)
        if not medicine:
            print("Medicine ID not found.")
            continue
        
        try:
            qty = int(input(f"Enter quantity for {medicine['name']}: "))
        except ValueError:
            print("Invalid quantity!")
            continue
        
        if qty > medicine["quantity"]:
            print(f"Not enough stock! Available quantity: {medicine['quantity']}")
            continue
        
        # Add to cart and reduce stock
        cart.append({"name": medicine["name"], "price": medicine["price"], "quantity": qty})
        medicine["quantity"] -= qty
        total_amount += medicine["price"] * qty
        print(f"Added {qty} x {medicine['name']} to cart.")
    
    # let's Show bill
    if cart:
        print("\n=== BILL ===")
        print(f"Customer: {customer_name}, Phone: {customer_phone}")
        for item in cart:
            print(f"{item['name']} x {item['quantity']} = Rs.{item['price'] * item['quantity']}")
        print(f"TOTAL: Rs.{total_amount}")
    else:
        print("No medicines purchased.")


# let's make a functionto show  Low Stock / Expired Check
def check_stock_expiry():
    """Show medicines with low stock or expired."""
    print("\n=== Low Stock / Expired Medicines ===")
    if not medicines:
        print("No medicines in store.")
        return
    today = input("Enter today's date (YYYY-MM-DD) to check expiry: ")
    for med in medicines:
        if med["quantity"] <= 5:
            print(f"Low Stock - {med['name']}, Quantity: {med['quantity']}")
        if med["expiry_date"] <= today:
            print(f"Expired - {med['name']}, Expiry: {med['expiry_date']}")

#let's make a main menu
def main_menu():
    while True:
        print("\n=== Pharmacy Store Management System ===")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Sell Medicine")
        print("4. Check Low Stock / Expired")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_medicine()
        elif choice == "2":
            view_medicines()
        elif choice == "3":
            sell_medicine()
        elif choice == "4":
            check_stock_expiry()
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()