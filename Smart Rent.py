import datetime

landlords = []
tenants = []
properties = []
rents = []
maintenance_req = []


def add_landlords():
    print("\n---- Add Landlord ----")
    name = input("Enter landlord name: ").strip().title()
    contact = input("Enter contact number: ").strip()
    email = input("Enter your email here: ").strip()

    landlord = {
        "name": name,
        "contact": contact,
        "email": email,
        "id": len(landlords) + 1
    }
    landlords.append(landlord)
    print(f"Landlord {name} added successfully!")


def view_landlords():
    print("\n--- List of Landlords ---")
    if not landlords:
        print("No landlords found yet..")
        return
    for l in landlords:
        print(f"ID: {l['id']} | Name: {l['name']} | Contact: {l['contact']} | Email: {l['email']}")


def add_tenant():
    print("\n== Add Tenant ==")
    name = input("Enter tenant name: ").strip().title()
    contact = input("Enter contact number: ").strip()
    email = input("Enter email here: ").strip()

    tenant = {
        "name": name,
        "contact": contact,
        "email": email,
        "id": len(tenants) + 1
    }
    tenants.append(tenant)
    print(f"Tenant {name} added successfully!")


def view_tenant():
    print("\n--- View Tenant ---")
    if not tenants:
        print("No tenant added yet!..")
        return
    for t in tenants:
        print(f"ID: {t['id']} | Name: {t['name']} | Contact: {t['contact']} | Email: {t['email']}")




def add_property():
    print("\n-- Add Property --")
    landlord_id = int(input("Enter landlord ID: ").strip())
    title = input("Enter property title: ").strip().title()
    address = input("Enter address: ").strip()
    rent = float(input("Enter monthly rent (in Rs): ").strip())
    status = "Available"

    property_data = {
        "id": len(properties) + 1,
        "landlord_id": landlord_id,
        "title": title,
        "address": address,
        "rent": rent,
        "status": status,
        "tenant_id": None
    }

    properties.append(property_data)
    print(f"Property '{title}' added successfully!")


def view_property():
    print("\n---- View Property ----")
    if not properties:
        print("No property added yet!...") 
        return
    for p in properties:
        tenant_name = next((t['name'] for t in tenants if t['id'] == p['tenant_id']), "None")
        print(f"ID: {p['id']} | Title: {p['title']} | Rent: Rs {p['rent']} | Status: {p['status']} | Tenant: {tenant_name}")


def assign_tenant():
    print("\n--- Assign Tenant ---")
    property_id = int(input("Enter property ID: ").strip())
    tenant_id = int(input("Enter tenant ID: ").strip())

    property_data = next((p for p in properties if p['id'] == property_id), None)
    if not property_data:
        print("Property not found...")
        return
    if property_data['status'] == "Rented":
        print("This property is already rented.")
        return

    property_data['tenant_id'] = tenant_id
    property_data['status'] = "Rented"
    print("Tenant assigned successfully!")




def record_rent_payment():
    print("\n--- Record Rent Payment ---")
    property_id = int(input("Enter property ID: ").strip())
    amount = float(input("Enter amount paid (Rs): ").strip())
    date = datetime.date.today()

    property_data = next((p for p in properties if p['id'] == property_id), None)
    if not property_data or not property_data['tenant_id']:
        print("Invalid property or no tenant assigned.")
        return

    payment = {
        "property_id": property_id,
        "tenant_id": property_data['tenant_id'],
        "amount": amount,
        "date": date
    }

    rents.append(payment)
    print("Rent payment added successfully!")


def view_rent_history():
    print("\n----- Rent History -----")
    if not rents:
        print("No rent payments recorded..")
        return
    for r in rents:
        tenant_name = next((t['name'] for t in tenants if t['id'] == r['tenant_id']), "Unknown")
        property_title = next((p['title'] for p in properties if p['id'] == r['property_id']), "Unknown")
        print(f"{tenant_name} paid Rs {r['amount']} for {property_title} on {r['date']}")




def add_maintenance_req():
    print("\n---- Maintenance Request ----")
    property_id = int(input("Enter property ID: ").strip())
    issue = input("Describe the issue: ").strip().capitalize()
    date = datetime.date.today()

    request = {
        "property_id": property_id,
        "issue": issue,
        "date": date,
        "status": "Pending"
    }
    maintenance_req.append(request)
    print("Maintenance request added successfully!")


def view_maintenance_req():
    print("\n---- Maintenance Requests ----")
    if not maintenance_req:
        print("No maintenance requests yet!...") 
        return
    for r in maintenance_req:
        property_title = next((p['title'] for p in properties if p['id'] == r['property_id']), "Unknown")
        print(f"Property: {property_title} | Issue: {r['issue']} | Status: {r['status']} | Date: {r['date']}")




def system_report():
    print("\n ------- System Report -------")
    print(f"Total Landlords: {len(landlords)}")
    print(f"Total Tenants: {len(tenants)}")
    print(f"Total Properties: {len(properties)}")
    print(f"Total Rented Properties: {sum(1 for p in properties if p['status'] == 'Rented')}")
    print(f"Total Rent Transactions: {len(rents)}")
    print(f"Pending Maintenance Requests: {sum(1 for r in maintenance_req if r['status'] == 'Pending')}")




def main_menu():
    while True:
        print("\n ===== Smart Rent & Property Management System =====")
        print("1. Add Landlord")
        print("2. Add Tenant")
        print("3. Add Property")
        print("4. View Properties")
        print("5. Assign Tenant to Property")
        print("6. Record Rent Payment")
        print("7. View Rent History")
        print("8. Add Maintenance Request")
        print("9. View Maintenance Requests")
        print("10. System Report")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            add_landlords()
        elif choice == "2":
            add_tenant()
        elif choice == "3":
            add_property()
        elif choice == "4":
            view_property()
        elif choice == "5":
            assign_tenant()
        elif choice == "6":
            record_rent_payment()
        elif choice == "7":
            view_rent_history()
        elif choice == "8":
            add_maintenance_req()
        elif choice == "9":
            view_maintenance_req()
        elif choice == "10":
            system_report()
        elif choice == "11":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
