import datetime
import json
import os

DATA_FILE = "khata_data.json"

# Load existing data if available
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        customers = json.load(f)
else:
    customers = []


def save_data():
    """Save current data to JSON file"""
    with open(DATA_FILE, "w") as f:
        json.dump(customers, f, indent=4, default=str)


def add_customer():
    print("\n==== Add Customer ====")
    name = input("Enter customer name: ").strip().title()
    phone = input("Enter customer number: ").strip()
    address = input("Enter customer address: ").strip().title()
    start_date = str(datetime.date.today())

    # Check if customer already exists
    for c in customers:
        if c["phone"] == phone:
            print("Customer with this phone number already exists!")
            return

    customer = {
        "name": name,
        "phone": phone,
        "address": address,
        "start_date": start_date,
        "transactions": []
    }

    customers.append(customer)
    save_data()
    print(f"Customer '{name}' added successfully!\n")


def record_transaction():
    print("\n==== Record Transaction ====")
    phone = input("Enter customer phone: ").strip()

    customer = next((c for c in customers if c["phone"] == phone), None)
    if not customer:
        print("No customer found! Please add the customer first.")
        return

    t_type = input("Enter transaction type (credit/payment): ").strip().lower()
    if t_type not in ["credit", "payment"]:
        print("Invalid type! Enter 'credit' or 'payment'.")
        return

    try:
        amount = float(input("Enter amount (Rs): "))
    except ValueError:
        print("Invalid amount entered!")
        return

    note = input("Enter note (optional): ").strip()
    date = str(datetime.date.today())

    transaction = {
        "type": t_type,
        "amount": amount,
        "note": note,
        "date": date
    }

    customer["transactions"].append(transaction)
    save_data()
    print(f"Transaction recorded for {customer['name']}.\n")


def view_summary():
    print("\n==== View Customer Summary ====")
    phone = input("Enter customer phone: ").strip()

    customer = next((c for c in customers if c["phone"] == phone), None)
    if not customer:
        print("Customer not found!")
        return

    total_credit = sum(t["amount"] for t in customer["transactions"] if t["type"] == "credit")
    total_payment = sum(t["amount"] for t in customer["transactions"] if t["type"] == "payment")
    balance = total_credit - total_payment

    print(f"\nSummary for {customer['name']}")
    print(f"Phone: {customer['phone']}")
    print(f"Address: {customer['address']}")
    print(f"Started: {customer['start_date']}")
    print("-" * 50)
    print(f"Total Credit : Rs.{total_credit:.2f}")
    print(f"Total Payment: Rs.{total_payment:.2f}")
    print(f"Remaining Due: Rs.{balance:.2f}")
    print("-" * 50)

    if customer["transactions"]:
        print("\nTransaction History:")
        for t in customer["transactions"]:
            print(f" - {t['date']}: {t['type'].capitalize()} Rs.{t['amount']} ({t['note']})")
    else:
        print("No transactions yet!")


def view_report():
    print("\n==== Overall Khata Report ====")
    if not customers:
        print("No customers found!")
        return

    print(f"{'Name':<20}{'Phone':<15}{'Credit':<15}{'Paid':<15}{'Balance':<15}")
    print("-" * 80)

    for c in customers:
        total_credit = sum(t["amount"] for t in c["transactions"] if t["type"] == "credit")
        total_payment = sum(t["amount"] for t in c["transactions"] if t["type"] == "payment")
        balance = total_credit - total_payment

        print(f"{c['name']:<20}{c['phone']:<15}{total_credit:<15.2f}{total_payment:<15.2f}{balance:<15.2f}")

    print("-" * 80)
    print(f"Report generated on: {datetime.date.today()}")


def main_menu():
    while True:
        print("\n===== DIGITAL KHATA MAIN MENU =====")
        print("1. Add Customer")
        print("2. Record Transaction")
        print("3. View Customer Summary")
        print("4. View Overall Report")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_customer()
        elif choice == "2":
            record_transaction()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            view_report()
        elif choice == "5":
            print("Exiting Digital Khata... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main_menu()
