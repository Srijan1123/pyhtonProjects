import datetime
import textwrap

students = []
rent = []
rooms = []
main_request = []
attendance_records = []

def next_id(lst):
    return len(lst) + 1

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        print("Invalid datetime format!...")
        return None

def today():
    return datetime.date.today()

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ").strip().title()
    contact = input("Enter contact number: ").strip()
    email = input("Enter email address (unique): ").strip().lower()
    address = input("Enter student address: ").strip().title()
    
    if any(s for s in students if s['email'] == email):
        print("Student with this email already exists..")
        return
    
    student = {
        "id": next_id(students),
        "name": name,
        "contact": contact,
        "email": email,
        "address": address,
        "room_no": None
    }
    students.append(student)
    print(f"Student added ID: {student['id']} | {student['name']}")

def list_students():
    print("\n--- Students ---")
    if not students:
        print("No student found. Add students first...")
        return
    for s in students:
        print(f"ID: {s['id']} | {s['name']} | Email: {s['email']} | Contact: {s['contact']} | Room: {s['room_no'] or None}")
        print()

def add_rooms():
    print("\n--- Add Rooms ---")
    room_no = input("Room number (e.g. A01): ").strip().upper()
    try:
        total_beds = int(input("Enter number of beds: ").strip())
    except ValueError:
        print("Invalid number of beds..")
        return
    if any(r for r in rooms if r['room_no'] == room_no):
        print("Room already exists..")
        return
    room = {
        "id": next_id(rooms),
        "room_no": room_no,
        "total_beds": total_beds,
        "occupied_beds": 0
    }
    rooms.append(room)
    print(f"Room {room_no} added with {total_beds} beds.")

def view_room():
    print("\n--- Rooms & Availability ---")
    if not rooms:
        print("No rooms added yet!...")
        return
    for r in rooms:
        available = r['total_beds'] - r['occupied_beds']
        status = "Full" if available == 0 else f"{available} available"
        print(f"{r['room_no']} | Beds: {r['occupied_beds']} / {r['total_beds']} | {status}")
        print()

def allocate_room():
    print("\n--- Allocate Bed To Student ---")
    if not students:
        print("No students added yet!...")
        return
    if not rooms:
        print("No rooms. Add rooms first..")
        return
    
    list_students()
    try:
        sid = int(input("Enter student ID to allocate room: ").strip())
    except ValueError:
        print("Invalid student ID")
        return
    
    student = next((s for s in students if s['id'] == sid), None)
    if not student:
        print("Student not found")
        return
    if student['room_no'] is not None:
        print(f"Student already assigned to room {student['room_no']}")
        return
    
    view_room()
    room_no = input("Enter room number to allocate: ").strip().upper()
    room = next((r for r in rooms if r['room_no'] == room_no), None)
    if not room:
        print("Room not found")
        return
    if room['occupied_beds'] >= room['total_beds']:
        print("No beds available in this room..")
        return
    
    room['occupied_beds'] += 1
    student['room_no'] = room_no
    print(f"Allocated room {room_no} to {student['name']} (ID: {student['id']})")

def record_rent_payment():
    print("\n--- Record Rent ---")
    if not students:
        print("No students available")
        return
    list_students()
    email = input("Enter student email (to record payment): ").strip()
    student = next((s for s in students if s['email'] == email), None)
    if not student:
        print("Student not found..")
        return
    if student['room_no'] is None:
        print("This student has no room assigned!")
        return
    
    try:
        amount = float(input("Enter amount paid (RS): ").strip())
    except ValueError:
        print("Invalid amount.")
        return
    
    date_str = input("Payment date (yyyy-mm-dd) [Leave blank for today]: ").strip()
    if date_str:
        date_val = parse_date(date_str)
        if not date_val:
            return
    else:
        date_val = today()
    
    payment = {
        "id": next_id(rent),
        "student_id": student['id'],
        "student_email": student['email'],
        "room_no": student['room_no'],
        "amount": amount,
        "date": date_val
    }
    rent.append(payment)
    print(f"Rent recorded: {student['name']} paid RS {amount} on {date_val} (Receipt ID: {payment['id']})")

def view_rent_history():
    print("\n--- Rent History ---")
    if not rent:
        print("No rent payments yet!..")
        return
    for r in rent:
        sname = next((s['name'] for s in students if s['id'] == r['student_id']), "Unknown")
        print(f"ID: {r['id']} | {r['date']} | {sname} | RS {r['amount']} | Room: {r['room_no'] or None}")
        print()

def lodge_maintenance():
    print("\n--- Lodge Maintenance Request ---")
    if not students:
        print("No students available")
        return
    list_students()
    try:
        sid = int(input("Enter student ID lodging complaint: ").strip())
    except ValueError:
        print("Invalid student ID")
        return
    
    student = next((s for s in students if s['id'] == sid), None)
    if not student:
        print("Student not found")
        return
    
    room_no = student['room_no'] or input("Student has no room assigned. Enter room number for the issue: ").strip().upper()
    issue = input("Describe the issue: ").strip()
    date_val = today()
    
    req = {
        "id": next_id(main_request),
        "student_id": student['id'],
        "student_name": student['name'],
        "room_no": room_no,
        "issue": issue,
        "date": date_val,
        "status": "Pending"
    }
    main_request.append(req)
    print(f"Maintenance request logged (ID: {req['id']})")

def view_maintenance():
    print("\n--- Maintenance Requests ---")
    if not main_request:
        print("No maintenance requests found.")
        return
    for req in main_request:
        print(f"ID: {req['id']} | {req['date']} | {req['student_name']} | Room: {req['room_no']} | Issue: {req['issue']} | Status: {req['status']}")
        print()

def resolve_maintenance():
    print("\n--- Resolve Maintenance Request ---")
    view_maintenance()
    try:
        rid = int(input("Enter request ID to mark resolved: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    req = next((r for r in main_request if r['id'] == rid), None)
    if not req:
        print("Request not found.")
        return
    if req['status'] == "Resolved":
        print("Request already resolved.")
        return
    req['status'] = "Resolved"
    print(f"Request {rid} marked as Resolved.")

def mark_attendence():
    print("\n ---  Mark Attendence ---")
    if not students:
        print("No student found!...")
        return
    list_students()
    try:
        sid = int(input("Enter student ID: ").strip())
    except ValueError:
        print("Invalid student ID..")
        return
    student = next((s for s in student if s['id'] == sid),None)
    if not student:
        print("student not found...")
        return
    else:
        date_val = today()
        status = input("status (in/out): ").strip().lower()
        if status not in ('in'/'out'):
            print("Status must be 'in" or'out')
            return
        
        rec = {
            "id":next_id(attendance_records),
            "student_id":student['id'],
            "student_name": student['name'],
            "date": date_val,
            "status": status
        }
        attendance_records.append(rec)
        print(f"Attendence recorded for {student['name']} on {date_val} as '{status}'.")
        
        
def view_attendence():
    print("\n --- Attendence Records ---")
    if not attendance_records:
        print("No attendence record..")
        return
    for a in attendance_records:
        print(f" ID:{a['id']} | {a['date']} | {a['student_name']} | {a['status']}")
        print()
        
def report_occupancy():
    total_beds = sum(r['total_beds'] for r in rooms)
    occupied = sum(r['occupied_beds'] for r in rooms)
    available = total_beds - occupied
    print("\n --- Occupancy Report --- ")
    print(f"Total Rooms: {len(rooms)} | Total beds: {total_beds} | occupancy: {occupied} | Available: {available}")
    
def report_weekly():
    print("\n ---  Weekly Report ---")
    cutoff  = today() - datetime.timedelta(days=7)
    
    rent_week = [p for p  in rent if p['date'] >= cutoff]
    maint_week = [m for m in main_request if m['date'] >=cutoff]
    attend_week = [a for a in attendance_records if a['date']>= cutoff]
    
    print(f"Rent payment in last 7 days : {len(rent_week)} | Total: Rs {sum(p['amount'] for p in rent_week):.2f}")
    print(f"Maintainance request in last 7 days: {len(maint_week)}")
    print(f"Attendence records in last 7 days:{len(attend_week)}")
    
    by_student = {}
    for p in rent_week:
        by_student[p['student_email']] = by_student.get(p['student_email'], 0) + p['amount']
    if by_student:
        print("\nRent by Students (week): ")
        for email, total in by_student.items():
            name = next((s for s in students if s['email'] == email),email)
            print(f" {name}:RS {total:.2f}")
            

def report_monthly():
    print("\n --- Monthly Report --- ")
    month_inp = input("Enter month and year (yyyy-mm-dd): ").strip()
    try:
        y,m  = map(int,month_inp.split("-"))
    except Exception:
        print("Invalid format")
        return
    
    rents_months = [p for p in rent if p['date'].year == y and p['date'].month == m]
    maint_month = [mreq for mreq in main_request if mreq['date'].year == y and mreq['date'].month == m]
    attend_month = [a for a in attendance_records if a['date'].year == y and a['date'].month == m]
    
    
    print(f"Rent payments in {month_inp}: {len(rents_months)} | Total: RS{sum(p['amount'] for p in rents_months):.2f}")
    print(f"Maintainance request in {month_inp}: {len(main_request)}")
    print(f"Attendence records in {month_inp}: {len(attend_month)}")
    
    
    
def main_menu():
    while True:
        print("\n ===== Main Menu =====")
        print("1. Add student")
        print("2. List student")    
        print("3. Add rooms")
        print("4. view rooms")
        print("5. Allocate bed to student")
        print("6. Record rent payment")
        print("7. View rent history")
        print("8. Lodge maintainance request")
        print("9. View maintainance requeust")
        print("10. Resolve maintainance request")
        print("11. Mark attendence")
        print("12. View attenndence records")
        print("13. occupancy reports")
        print("14. weekly report")
        print("15. monthly report")
        print("16. Exit")
        
        choice = input("Enter your choice (1-16): ").strip()
        
        if choice == "1":
            add_student()
            
        elif choice =="2":
            list_students()
            
        elif choice == "3":
            add_rooms()
            
        elif choice =="4":
            view_room()
            
        elif choice =="5":
            allocate_room()
            
        elif choice =="6":
            record_rent_payment()
            
        elif choice =="7":
            view_rent_history()
            
        elif choice =="8":
            lodge_maintenance()
            
        elif choice =="9":
            view_maintenance()
            
        elif choice =="10":
            resolve_maintenance()
            
        elif choice =="11":
            mark_attendence()
            
        elif choice =="12":
            view_attendence()
            
        elif choice =="13":
            report_occupancy()
            
        elif choice =="14":
            report_weekly()
            
        elif choice =="15":
            report_monthly()
            
        elif choice =="16":
            print("Exiting system...")
            
        else:
            print("Invalid choice. Try again!...")  
            
            
if __name__ == "__main__":
    main_menu()
        