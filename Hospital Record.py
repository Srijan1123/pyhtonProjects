patient = []
next_id = 1

# Now let's add patient
def add_patient():  
    global next_id
    print("\==Add Patient")
    name = input("Enter your name: ").strip()
    phone = input("Enter your phone number: ").strip()
    age = input("Enter your age: ").strip()
    gender = input("Enter gender (M/F): ").strip()
    doctor = input("Enter appointed doctor name: ").strip()
    symptoms = input("Enter a patient symptoms: ").strip()
    
    new_patient = {
        "id": next_id,
        "name": name,
        "phone": phone,
        "gender": gender,
        "age": age,
        "doctor": doctor,
        "symptoms": symptoms
    }
    patient.append(new_patient)
    print(f"Patient record added successfully!..")
    next_id += 1
    
# let's view all patients
def view_patients():
    if not patient:
        print("No patients recorded yet!..")
        return
    print("\n==All Patients Record")
    print(f"{'id':<3} {'name':15} {'age':<5} {'gender':<6} {'doctor':15} {'symptoms'}")
    print("-" * 60)
    for p in patient:
        print(f"{p['id']:<3} {p['name']:15} {p['age']:<5} {p['gender']:<6} {p['doctor']:15} {p['symptoms']}")
    print("-" * 60)    
    
# let's view doctor
def view_doctor():
    doctor = input("Enter doctor name: ").strip()
    results = [p for p in patient if p['doctor'].lower() == doctor.lower()]
    if not results:
        print(f"\nNo patients found for doctor {doctor}.")
        return
    print(f"\n=== Patients for doctor {doctor} ===")
    for p in results:
        print(f"{p['id']}. {p['name']} {p['symptoms']}")
        
# let's view symptoms now
def view_symptoms():
    symptoms = input("Enter a symptom here: ").strip()
    results = [p for p in patient if p['symptoms'].lower() == symptoms.lower()]
    if not results:
        print(f"\nNo patient found with these symptoms {symptoms}.")
        return
    print(f"\n=== Patients with {symptoms} === ")
    for p in results:
        print(f"{p['id']}. {p['name']} (Doctor: {p['doctor']})")

# Now let's make main menu()
def main_menu():
    while True:
        print("\n----Hospital patient record system----")
        print("1. Add patient")
        print("2. View all patient")
        print("3. View patient by doctor")
        print("4. View patient by symptoms")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            view_doctor()
        elif choice == "4":
            view_symptoms()
        elif choice == "5":
            print("Exiting system!...") 
            break
        else:
            print("Invalid choice...")

if __name__ == "__main__":
    main_menu()
