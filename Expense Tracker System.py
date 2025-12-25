import datetime

expense = []

def add_expenses():
    print("\n=== Add Your Expenses Here ===")
    name = input("Enter expense name: ").strip().title()
    try:
        amount = float(input("Enter amount (Rs): "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    category = input("Enter category (Food, Travel, Shopping, etc): ").strip().title()
    date_input = input("Enter date (yyyy-mm-dd) or leave blank for today: ").strip()
    
    if date_input:
        try:
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format! Please use yyyy-mm-dd.")
            return
    else:
        date = datetime.date.today()
    
    expense.append({
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    })
            
    print(f" Expense '{name}' of Rs.{amount:.2f} added under '{category}' category for {date}.\n")


def view_expense():
    print("\n-- All Expenses --")
    if not expense:
        print("No expenses recorded yet!")
        return
    
    print(f"{'Name':<15}{'Amount':<10}{'Category':<15}{'Date'}")
    print("-" * 55)
    
    for exp in expense:
        print(f"{exp['name']:<15}{exp['amount']:<10.2f}{exp['category']:<15}{exp['date']}")
    print("-" * 55)


def view_summary():
    print("\n--- View Summary ---")
    if not expense:
        print("No expenses recorded yet!")
        return
    
    date_input = input("Enter date (yyyy-mm-dd) to view summary: ").strip()
    try:
        selected_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format!")
        return
    
    total = 0
    print(f"\nExpenses for {selected_date}:")
    print(f"{'Name':<20}{'Amount':<10}{'Category':<15}")
    print("-" * 50)
    
    for exp in expense:
        if exp['date'] == selected_date:
            print(f"{exp['name']:<20}{exp['amount']:<10.2f}{exp['category']:<15}")
            total += exp['amount']
    
    print("-" * 50)
    print(f"Total spent: Rs.{total:.2f}\n")


def daily_summary():
    print("\n-- Daily Summary ---")
    if not expense:
        print("No expenses recorded yet!")
        return
    
    date_input = input("Enter date (yyyy-mm-dd) to view summary: ").strip()
    try:
        selected_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format!")
        return
    
    total = 0
    print(f"\nExpenses for {selected_date}:")
    print(f"{'Name':<20}{'Amount':<10}{'Category':<15}")
    print("-" * 50)
    
    for exp in expense:
        if exp['date'] == selected_date:
            print(f"{exp['name']:<20}{exp['amount']:<10.2f}{exp['category']:<15}")
            total += exp['amount']
    
    print("-" * 50)
    print(f"Total spent: Rs.{total:.2f}\n")


def monthly_summary():
    print("\n-- Monthly Summary --")
    if not expense:
        print("No expenses recorded yet!")
        return

    month_input = input("Enter month and year (yyyy-mm): ").strip()
    try:
        year, month = map(int, month_input.split("-"))
    except ValueError:
        print("Invalid format! Use yyyy-mm.")
        return
    
    total = 0
    print(f"\nExpenses for {month_input}:")
    print(f"{'Name':<20}{'Amount':<10}{'Category':<15}{'Date'}")
    print("-" * 60)
    
    for exp in expense:
        if exp['date'].year == year and exp['date'].month == month:
            print(f"{exp['name']:<20}{exp['amount']:<10.2f}{exp['category']:<15}{exp['date']}")
            total += exp['amount']
    
    print("-" * 60)
    print(f"Total monthly spending: Rs.{total:.2f}\n")
            

def main_menu():
    while True:
        print("\n== Welcome to Main Menu ==")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Daily Summary")
        print("4. Monthly Summary")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            daily_summary()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main_menu()
