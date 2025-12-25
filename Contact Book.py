contact = {}

# let's add the contact
def add_contact():
    print("\n---Add Contact----")
    name = input("Enter your name : ").strip()
    phone = input("Enter your number : ").strip()
    email = input("Enter your email: ").strip()
    address = input("Enter your address: ").strip()
    contact[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact {name} added successfully!...")
    
# let's view the contact
def view_contact():
    if not contact:
        print("\n--No contact added yet!---")
        return
    else:
        print("\n--Contact List--")
        for name, info in contact.items():
            print(f"\nName: {name}")
            for key, value in info.items():
                print(f"{key}: {value}")
        print()
                
# let's search contact
def search_contact():
    name = input("Enter the name to search: ").strip()
    if name in contact:
        print(f"\n--Found contact for {name}: --")
        for key, value in contact[name].items():
            print(f"{key}: {value}")
    else:
        print("\n--Contact not found--")
                
# let's update the contact 
def update_contact():
    if not contact:
        print("\n--No contact found--")
        return
    name = input("Enter contact name to update: ").strip()
    if name in contact:
        print("\n--Leave field blank to keep current value.--")
        phone = input("New phone (or press Enter to skip): ").strip()
        email = input("New email (or press Enter to skip): ").strip()
        address = input("New address (or press Enter to skip): ").strip()
        
        if phone: contact[name]['phone'] = phone
        if email: contact[name]['email'] = email
        if address: contact[name]['address'] = address
        print(f"\n--Contact {name} updated successfully!---\n")
    else:
        print("\n--Contact not found--")
            
# let's delete the contact
def delete_contact():
    name = input("Enter contact to delete: ").strip()
    if name in contact:
        del contact[name]
        print(f"\n--Contact {name} deleted successfully!---")
    else:
        print("\n--Contact not found--")
        
# let's make the main menu
def main_menu():
    while True:
        print("\n-----Main Menu-----")
        print("1. Add contact")
        print("2. View contact")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_contact()
            
        elif choice == "2":
            view_contact()
            
        elif choice == "3":
            search_contact()
            
        elif choice == "4":
            update_contact()
            
        elif choice == "5":
            delete_contact()
            
        elif choice == "6":
            print("Exiting system...")
            
        else:
            print("Invalid choice. Try again...")
            
if __name__ == "__main__":
    main_menu()
