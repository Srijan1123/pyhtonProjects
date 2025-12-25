courses = {}

# Let's add the course
def add_course():
    print("\n---Add Course Here---")
    course_name = input("Enter a course name: ").strip().title()
    
    if course_name in courses:
        print("This course is already here!...")
        return
    
    courses[course_name] = {'participants': []}
    print(f"Course '{course_name}' added successfully!...\n")
    

# Let's register participants
def register_participants():
    print("\n--Register Here---")
    if not courses:
        print("No courses available right now!...")
        return
    
    name = input("Enter participant's name: ").strip().title()
    
    print("\n--Available Courses--")
    for i, course in enumerate(courses.keys(), start=1):
        print(f"{i}. {course}")
    
    try:
        choice = int(input("Select by course number: "))
        course_list = list(courses.keys())
        selected_course = course_list[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice!\n")
        return
    
    if name in courses[selected_course]['participants']:
        print(f"{name} is already registered in {selected_course}!\n")
        return
    
    courses[selected_course]['participants'].append(name)
    print(f"{name} successfully registered for {selected_course}!\n")


# Let's view all of the courses with participants count
def view_course():
    print("\n---Courses Overview---")
    if not courses:
        print("No courses added yet!...")
        return
    
    print(f"{'Course Name':<25}{'Participants Count':<10}")
    print("-" * 40)
    
    for cname, details in courses.items():
        count = len(details['participants'])
        print(f"{cname:<25}{count:<10}")
    print()


# Let's view the participants per course
def view_participants():
    print("\n----View Participants----")
    if not courses:
        print("No course available!..")
        return
    
    for cname, details in courses.items():
        print(f"\nCourse: {cname}")
        print("-" * (len(cname) + 8))
        if details['participants']:
            for idx, name in enumerate(details['participants'], start=1):
                print(f"{idx}. {name}")
        else:
            print("No participants yet!..")
    print()


# Main menu
def main_menu():
    while True:
        print("\n----Main Menu----")
        print("1. Add Course")
        print("2. Register Participants")
        print("3. View Course Overview")
        print("4. View Participants per Course")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_course()
        elif choice == "2":
            register_participants()
        elif choice == "3":
            view_course()
        elif choice == "4":
            view_participants()
        elif choice == "5":
            print("Exiting System.... Goodbye!")
            break
        else:
            print("Invalid choice. Try again!..")

if __name__ == "__main__":
    main_menu()
