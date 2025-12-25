# Store students and attendance
students = []
attendance_records = []
next_student_id = 1

#let's add the students
def add_student():
    global next_student_id
    print("\n=== Add Student ===")
    name = input("Enter student name: ")
    class_name = input("Enter class/grade: ")
    roll_number = input("Enter roll number: ")

    student = {
        "student_id": next_student_id,
        "name": name,
        "class": class_name,
        "roll_number": roll_number
    }

    students.append(student)
    print(f"Student added successfully! Student ID = {next_student_id}")
    next_student_id += 1

# Let's mark the attendence
def mark_attendance():
    if not students:
        print("No students registered yet!")
        return

    import datetime
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"\n=== Mark Attendance for {today} ===")

    for student in students:
        status = input(f"Mark attendance for {student['name']} (P/A): ").strip().upper()
        if status not in ["P", "A"]:
            status = "A"  # Default Absent if invalid
        record = {
            "student_id": student["student_id"],
            "date": today,
            "status": status
        }
        attendance_records.append(record)

    print("Attendance marked successfully!")

#Let's view the attendence records
def view_attendance():
    if not attendance_records:
        print("No attendance records found!")
        return

    print("\n=== Attendance Records ===")
    for record in attendance_records:
        student = next(s for s in students if s["student_id"] == record["student_id"])
        print(f"Date: {record['date']}, Student: {student['name']}, Status: {record['status']}")

# Let's calculate attendence in percentage
def calculate_attendance_percentage():
    if not students:
        print("No students available!")
        return

    print("\n=== Attendance Percentage ===")
    for student in students:
        total_days = len([r for r in attendance_records if r["student_id"] == student["student_id"]])
        present_days = len([r for r in attendance_records if r["student_id"] == student["student_id"] and r["status"] == "P"])
        
        percentage = (present_days / total_days * 100) if total_days > 0 else 0
        print(f"{student['name']} (ID: {student['student_id']}): {percentage:.2f}%")

#Let's generate the report
def generate_report():
    print("\n=== Attendance Report ===")
    calculate_attendance_percentage()

#let's make the main menu
def main_menu():
    while True:
        print("\n===== School Attendance System =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance Records")
        print("4. Calculate Attendance Percentage")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            calculate_attendance_percentage()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main_menu()
