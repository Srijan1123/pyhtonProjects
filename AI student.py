import datetime
import textwrap
from collections import defaultdict

students = []             
study_sessions = []       


def next_id(lst):
    return len(lst) + 1

def today():
    return datetime.date.today()

def parse_date(s):
    s = s.strip()
    if not s:
        return None
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d").date()
    except Exception:
        print("Invalid date format. Use YYYY-MM-DD.")
        return None

def add_student():
    print("\n--- Add Student ---")
    name = input("Full name: ").strip().title()
    email = input("Email (unique): ").strip().lower()
    course = input("Course / Level (optional): ").strip().title()
    if any(x for x in students if x['email'] == email):
        print("Student with this email already exists.")
        return
    stud = {
        "id": next_id(students),
        "name": name,
        "email": email,
        "course": course,
        "created": today()
    }
    students.append(stud)
    print(f"Student added: ID {stud['id']} | {stud['name']}")

def list_students():
    print("\n--- Students ---")
    if not students:
        print("No students registered.")
        return
    for s in students:
        print(f"ID:{s['id']} | {s['name']} | {s['email']} | {s['course']}")

def log_session():
    print("\n--- Log Study Session ---")
    if not students:
        print("No students. Add a student first.")
        return
    list_students()
    try:
        sid = int(input("Enter student ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    student = next((s for s in students if s['id'] == sid), None)
    if not student:
        print("Student not found.")
        return

    date_input = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()
    if date_input == "":
        date_val = today()
    else:
        date_val = parse_date(date_input)
        if not date_val:
            return

    subject = input("Subject / Topic: ").strip().title()
    try:
        duration = int(input("Duration (minutes): ").strip())
    except ValueError:
        print("Invalid duration.")
        return
    # distraction level: 0 (none) - 5 (very distracted)
    try:
        distraction = int(input("Distraction level 0-5 (0=none,5=high): ").strip())
        if distraction < 0 or distraction > 5:
            raise ValueError
    except ValueError:
        print("Invalid distraction level.")
        return

    try:
        focus = int(input("Focus rating 0-5 (0=poor,5=excellent): ").strip())
        if focus < 0 or focus > 5:
            raise ValueError
    except ValueError:
        print("Invalid focus rating.")
        return

    session = {
        "id": next_id(study_sessions),
        "student_id": sid,
        "date": date_val,
        "subject": subject,
        "duration": duration,
        "distraction": distraction,
        "focus": focus
    }
    study_sessions.append(session)
    print(f"Logged: {duration} min on {subject} for {student['name']} ({date_val}).")


def sessions_for_student(sid, start_date=None, end_date=None):
    res = [s for s in study_sessions if s['student_id'] == sid]
    if start_date:
        res = [s for s in res if s['date'] >= start_date]
    if end_date:
        res = [s for s in res if s['date'] <= end_date]
    return res

def summarize_sessions(sessions):
    total_minutes = sum(s['duration'] for s in sessions)
    count = len(sessions)
    avg_focus = (sum(s['focus'] for s in sessions) / count) if count else 0
    avg_distraction = (sum(s['distraction'] for s in sessions) / count) if count else 0
    by_subject = defaultdict(int)
    for s in sessions:
        by_subject[s['subject']] += s['duration']
    return {
        "total_minutes": total_minutes,
        "session_count": count,
        "avg_focus": round(avg_focus,2),
        "avg_distraction": round(avg_distraction,2),
        "by_subject": dict(by_subject)
    }


def student_report():
    print("\n--- Student Report ---")
    if not students:
        print("No students yet.")
        return
    list_students()
    try:
        sid = int(input("Enter student ID for report: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    student = next((s for s in students if s['id'] == sid), None)
    if not student:
        print("Student not found.")
        return

   
    start = input("Start date (YYYY-MM-DD) [leave blank = 7 days ago]: ").strip()
    if start == "":
        start_date = today() - datetime.timedelta(days=7)
    else:
        start_date = parse_date(start)
        if not start_date:
            return
    end = input("End date (YYYY-MM-DD) [leave blank = today]: ").strip()
    end_date = today() if end == "" else parse_date(end)
    if end_date is None:
        return

    sess = sessions_for_student(sid, start_date, end_date)
    summary = summarize_sessions(sess)
    print(f"\nReport for {student['name']} ({start_date} → {end_date})")
    print(f"Total study time: {summary['total_minutes']} minutes in {summary['session_count']} sessions")
    print(f"Average focus: {summary['avg_focus']} /5  |  Avg distraction: {summary['avg_distraction']} /5")
    if summary['by_subject']:
        print("\nTime by subject:")
        for sub, m in summary['by_subject'].items():
            print(f" - {sub}: {m} minutes")
    else:
        print("No sessions in this range.")
    print()

    suggestions = analyze_habits(sid, summary)
    print("Suggestions:")
    for s in suggestions:
        print(" - " + s)
    print()


def analyze_habits(sid, summary=None):
    # rule-based suggestions (explainable)
    if summary is None:
        sess = sessions_for_student(sid)
        summary = summarize_sessions(sess)

    suggestions = []
    total_minutes = summary['total_minutes']
    avg_focus = summary['avg_focus']
    avg_distraction = summary['avg_distraction']
    session_count = summary['session_count']

   
    today_date = today()
    last_7 = [s for s in sessions_for_student(sid, today_date - datetime.timedelta(days=6), today_date)]
    days_with_sessions = set(s['date'] for s in last_7)
    streak = len(days_with_sessions)

    
    if total_minutes < 30:
        suggestions.append("You studied less than 30 minutes in the selected period. Try 25-45 min focused sessions daily.")
    elif total_minutes < 120:
        suggestions.append("Good start — aim for consistent daily sessions to build momentum (target 2–4 sessions/week to start).")
    else:
        suggestions.append("Nice total study minutes. Keep it up — focus on quality & spaced review.")

    if avg_focus < 3:
        suggestions.append("Focus scores are low. Remove distractions (phone away), use a 25-minute Pomodoro, then 5-min break.")
    if avg_distraction > 2:
        suggestions.append("High distraction levels detected. Try environment changes: quieter space or noise-cancelling music.")
    if streak >= 5:
        suggestions.append(f"Great consistency: you studied on {streak} of the last 7 days. Maintain the streak!")
    elif streak >= 2:
        suggestions.append(f"You studied on {streak} of the last 7 days. Aim for at least 4 days for a habit to form.")
    else:
        suggestions.append("Your routine is irregular. Pick fixed daily time slots and protect them as appointments.")

   
    by_sub = summary.get('by_subject', {})
    if by_sub:
        primary = max(by_sub.items(), key=lambda x: x[1])[0]
        suggestions.append(f"You spend most time on '{primary}'. Ensure you review weaker subjects too (rotate subjects).")

    recommended_plan = recommend_next_day_plan(sid, summary)
    suggestions.append("Recommended next-day plan:")
    for rp in recommended_plan:
        suggestions.append(f"  • {rp['subject']}: {rp['duration']} min ({rp['type']})")

    return suggestions

def recommend_next_day_plan(sid, summary=None):
    
    if summary is None:
        sess = sessions_for_student(sid, today() - datetime.timedelta(days=7), today())
        summary = summarize_sessions(sess)

    by_sub = summary.get('by_subject', {})
    if not by_sub:
   
        return [
            {"subject": "Review / Planning", "duration": 30, "type": "Planning & Light Review"},
            {"subject": "Main Subject", "duration": 60, "type": "Active Study (Pomodoro)"}
        ]

    
    subs = sorted(by_sub.items(), key=lambda x: x[1])
    total_minutes = max(90, summary['total_minutes'])  # try ~90 minutes target
    plan = []
    # allocate proportional but favor smaller ones
    remaining = total_minutes
    for i, (sub, _) in enumerate(subs):
        if i == len(subs) - 1:
            dur = remaining
        else:
            dur = max(20, int(total_minutes / (len(subs) + 1)))  # base allocation
        plan.append({"subject": sub, "duration": dur, "type": "Active Study"})
        remaining -= dur
        if remaining <= 0:
            break
    # if only one subject, add a secondary small block
    if len(plan) == 1:
        plan.append({"subject": "Flashcards / Quick Practice", "duration": 20, "type": "Recall"})
    return plan

def system_summary():
    print("\n--- System Summary ---")
    total_students = len(students)
    total_sessions = len(study_sessions)
    total_minutes = sum(s['duration'] for s in study_sessions)
    print(f"Students: {total_students} | Sessions logged: {total_sessions} | Total minutes: {total_minutes}")
    # top students by study minutes (last 30 days)
    cutoff = today() - datetime.timedelta(days=30)
    by_student = defaultdict(int)
    for s in study_sessions:
        if s['date'] >= cutoff:
            by_student[s['student_id']] += s['duration']
    if by_student:
        sorted_by = sorted(by_student.items(), key=lambda x: x[1], reverse=True)[:5]
        print("\nTop students (last 30 days):")
        for sid, mins in sorted_by:
            name = next((st['name'] for st in students if st['id'] == sid), "Unknown")
            print(f" - {name}: {mins} minutes")
    print()


def main_menu():
    while True:
        print("\n=== AI Study Habit Analyzer ===")
        print("1. Add student")
        print("2. List students")
        print("3. Log study session")
        print("4. Student report & suggestions")
        print("5. System summary")
        print("6. Quick demo data (populate sample)")
        print("7. Exit")
        choice = input("Choose (1-7): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            log_session()
        elif choice == "4":
            student_report()
        elif choice == "5":
            system_summary()
        elif choice == "6":
            populate_demo()
        elif choice == "7":
            print("Exiting. Keep studying!")
            break
        else:
            print("Invalid choice. Try again.")


def populate_demo():
    # small dataset to demo features
    students.clear()
    study_sessions.clear()
    # add students
    students.append({"id":1,"name":"Srijan","email":"srijan02@hehehehe.com","course":"Grade12","created":today()})
    students.append({"id":2,"name":"Bikash","email":"bikash01@hahaha.com","course":"Bachelors","created":today()})
    # add sessions for Asha (mix)
    base = today() - datetime.timedelta(days=6)
    for i,mins,focus,dis in [(0,40,4,1),(1,30,3,2),(2,50,5,0),(3,20,2,3),(4,60,4,1),(5,25,3,2),(6,35,4,1)]:
        study_sessions.append({
            "id": next_id(study_sessions),
            "student_id": 1,
            "date": base + datetime.timedelta(days=i),
            "subject": "Math" if i%2==0 else "Physics",
            "duration": mins,
            "distraction": dis,
            "focus": focus
        })
   
    study_sessions.append({
        "id": next_id(study_sessions),
        "student_id": 2,
        "date": today(),
        "subject": "English",
        "duration": 25,
        "distraction": 1,
        "focus": 4
    })
    print("Demo data populated (2 students, several sessions).")


if __name__ == "__main__":
    main_menu()