import datetime

solar_system = []
energy_logs = []


def add_solar_system():
    print("\n=== Add Solar System ===")
    system_id = input("Enter system ID: ").strip().upper()
    location = input("Enter location: ").strip().title()
    owner = input("Enter owner name: ").strip().title()

    try:
        capacity = float(input("Enter panel capacity (kW): "))
    except ValueError:
        print("Invalid capacity! Must be a number.")
        return

    install_date = input("Enter installation date (yyyy-mm-dd): ").strip()
    try:
        install_date = datetime.datetime.strptime(install_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format! Use yyyy-mm-dd.")
        return

    solar_system.append({
        "system_id": system_id,
        "location": location,
        "owner": owner,
        "capacity": capacity,
        "install_date": install_date
    })
    print(f"Solar system {system_id} added successfully!\n")


def log_daily_data():
    print("\n=== Daily Log ===")
    if not solar_system:
        print("Add solar system first...")
        return

    system_id = input("Enter system ID to log data for: ").strip().upper()
    system = next((s for s in solar_system if s["system_id"] == system_id), None)
    if not system:
        print("System not found!")
        return

    date_input = input("Enter date (yyyy-mm-dd) or leave blank for today: ").strip()
    if date_input:
        try:
            log_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format!")
            return
    else:
        log_date = datetime.date.today()

    try:
        generated = float(input("Enter energy generated (kWh): "))
        consumed = float(input("Enter consumed energy (kWh): "))
        battery = float(input("Enter battery health (%): "))
        efficiency = float(input("Enter system efficiency (%): "))
    except ValueError:
        print("Invalid numeric value! Try again.")
        return

    energy_saved = max(generated - consumed, 0)
    savings = energy_saved * 15

    status = "System Running Smoothly"
    if battery <= 40:
        status = "Low Battery Alert"
    elif battery <= 60:
        status = "Battery Maintenance Required"

    energy_logs.append({
        "system_id": system_id,
        "date": log_date,
        "generated": generated,
        "consumed": consumed,
        "battery": battery,
        "efficiency": efficiency,
        "saved": energy_saved,
        "savings": savings,
        "status": status
    })

    print(f"\nLog added for system {system_id} on {log_date}")
    print(f"Status: {status}\n")


def view_system():
    print("\n=== View Systems ===")
    if not solar_system:
        print("No systems found!")
        return

    print(f"{'System ID':<10} {'Owner':<20} {'Location':<20} {'Capacity(kW)':<15} {'Installed On'}")
    print("-" * 80)
    for s in solar_system:
        print(f"{s['system_id']:<10} {s['owner']:<20} {s['location']:<20} {s['capacity']:<15} {s['install_date']}")
    print("-" * 80)


def view_log():
    print("\n=== Energy Logs ===")
    if not energy_logs:
        print("No energy logs found.")
        return
    print(f"{'System ID':<10} {'Date':<15} {'Generated':<15} {'Consumed':<15} {'Battery(%)':<15} {'Status'}")
    print("-" * 90)
    for l in energy_logs:
        print(f"{l['system_id']:<10} {l['date']:<15} {l['generated']:<15.2f} {l['consumed']:<15.2f} {l['battery']:<15.2f} {l['status']}")
    print("-" * 90)


def generate_report():
    print("\n=== Generate Report ===")
    if not energy_logs:
        print("No energy logs found...")
        return

    total_generated = sum(log["generated"] for log in energy_logs)
    total_consumed = sum(log["consumed"] for log in energy_logs)
    avg_battery = sum(log["battery"] for log in energy_logs) / len(energy_logs)
    avg_efficiency = sum(log["efficiency"] for log in energy_logs) / len(energy_logs)
    total_savings = sum(log["savings"] for log in energy_logs)

    print(f"Total Energy Generated:  {total_generated:.2f} kWh")
    print(f"Total Energy Consumed:   {total_consumed:.2f} kWh")
    print(f"Average Battery Health:  {avg_battery:.2f}%")
    print(f"Average Efficiency:      {avg_efficiency:.2f}%")
    print(f"Total Estimated Savings: Rs. {total_savings:.2f}")
    print("-" * 60)

    if avg_battery <= 40:
        print("Overall battery health is LOW - Consider maintenance.")
    elif avg_battery <= 60:
        print("System efficiency is below normal - check solar panels.")
    else:
        print("All systems are operating efficiently.\n")


def main_menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Add Solar System")
        print("2. Log Daily Energy Data")
        print("3. View All Systems")
        print("4. View Energy Log")
        print("5. Generate Analytical Report")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            add_solar_system()
        elif choice == "2":
            log_daily_data()
        elif choice == "3":
            view_system()
        elif choice == "4":
            view_log()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
