import datetime

students = []
internships = []
applications = []

def add_student():
    print("\n=== Add Student ===")
    name = input("Enter student name: ").strip().title()
    course = input("Enter course name: ").strip().title()
    skills = input("Enter your skills (comma separated): ").lower().split(",")
    certification = input("Enter certification (if any, comma separated): ").strip().split(",")

    student = {
        "name": name,
        "course": course,
        "skills": [s.strip() for s in skills],
        "certification": [c.strip() for c in certification],
        "verified": False
    }

    students.append(student)
    print(f" Student {name} added successfully!\n")


def view_student():
    print("\n=== View Students ===")
    if not students:
        print("No students added yet!\n")
        return

    for i, s in enumerate(students, start=1):
        status = "Verified" if s['verified'] else "Not Verified"
        print(f"{i}. {s['name']} - {s['course']} ({status})")

    try:
        choice = int(input("Enter student number to verify: "))
        students[choice - 1]['verified'] = True
        print(f"🎓 {students[choice - 1]['name']} is now verified!\n")
    except (ValueError, IndexError):
        print("Invalid input! Try again.\n")


def add_internship():
    print("\n=== Add Internship Opportunity ===")
    company = input("Enter company name: ").strip().title()
    title = input("Enter internship title: ").strip().title()
    skills_req = input("Enter required skills (comma separated): ").strip().split(",")
    duration = input("Enter duration (e.g., 3 months): ").strip()
    stipend = input("Enter stipend (in Rs or 'Unpaid'): ").strip()

    internship = {
        "company": company,
        "title": title,
        "skills": [s.strip() for s in skills_req],
        "duration": duration,
        "stipend": stipend,
        "posted_on": datetime.date.today()
    }

    internships.append(internship)
    print(f" Internship '{title}' at {company} added successfully!\n")


def match_internship():
    print("\n=== Match Internship ===")
    if not students or not internships:
        print("Add both students and internships first!\n")
        return

    name = input("Enter student name to find matches: ").strip().title()
    student = next((s for s in students if s["name"] == name), None)

    if not student:
        print("Student not found!\n")
        return

    matched = []
    for intern in internships:
        overlap = set(student['skills']) & set(intern['skills'])
        if overlap:
            matched.append((intern, len(overlap)))

    if not matched:
        print(f"No matches found for {name}.\n")
    else:
        matched.sort(key=lambda x: x[1], reverse=True)
        print(f"\nTop Internship Matches for {name}:\n")
        print(f"{'Company':<20} {'Title':<25} {'Matched Skills':<20} {'Stipend'}")
        print("-" * 80)
        for job, score in matched:
            print(f"{job['company']:<20} {job['title']:<25} {score:<20} {job['stipend']}")
        print("-" * 80)
        print()


def apply_internship():
    print("\n=== Apply for Internship ===")
    if not students or not internships:
        print("Add data first!\n")
        return

    name = input("Enter student name: ").strip().title()
    company = input("Enter company name: ").strip().title()

    student = next((s for s in students if s['name'] == name), None)
    internship = next((i for i in internships if i['company'] == company), None)

    if not student or not internship:
        print("Invalid student or company name.\n")
        return

    applications.append({
        "student": name,
        "company": company,
        "title": internship['title'],
        "status": "Applied",
        "date": datetime.date.today()
    })
    print(f" {name} successfully applied for {internship['title']} at {company}!\n")


def view_reports():
    print("\n=== System Report ===")
    print(f"Total Students: {len(students)}")
    print(f"Verified Students: {sum(1 for s in students if s['verified'])}")
    print(f"Internships Available: {len(internships)}")
    print(f"Applications Made: {len(applications)}\n")


def main_menu():
    while True:
        print("\n===== Student Skill Portfolio & Internship Finder =====")
        print("1. Add Student")
        print("2. Verify Student Portfolio")
        print("3. Add Internship")
        print("4. Match Internship")
        print("5. Apply for Internship")
        print("6. View Reports")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            add_internship()
        elif choice == "4":
            match_internship()
        elif choice == "5":
            apply_internship()
        elif choice == "6":
            view_reports()
        elif choice == "7":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main_menu()
