"""
Add Students Script
Automatically populate Google Sheets with multi-subject student data.
Run this to quickly add realistic student records for testing.
"""

from integrations.google_sheets import get_sheet
from config import settings
from utils.helpers import setup_logger
from datetime import datetime

logger = setup_logger(__name__)

# Subjects taught at the school
SUBJECTS = [
    "Mathematics",
    "English",
    "Science", 
    "History",
    "Art",
    "Physical Education"
]

# Sample student data with realistic multi-subject records
SAMPLE_STUDENTS = [
    {
        "name": "Emma Johnson",
        "subjects": {
            "Mathematics": {"score": 85, "attendance": "95%", "notes": "Strong algebraic thinking, needs work on geometry", "behavior": "Excellent"},
            "English": {"score": 88, "attendance": "92%", "notes": "Excellent creative writing, good comprehension skills", "behavior": "Excellent"},
            "Science": {"score": 90, "attendance": "96%", "notes": "Outstanding lab participation, curious learner", "behavior": "Excellent"},
            "History": {"score": 82, "attendance": "90%", "notes": "Good understanding of timelines, participates well", "behavior": "Good"},
            "Art": {"score": 78, "attendance": "88%", "notes": "Shows creativity, improving technical skills", "behavior": "Good"},
            "Physical Education": {"score": 92, "attendance": "98%", "notes": "Athletic, great team player, leadership qualities", "behavior": "Excellent"}
        }
    },
    {
        "name": "Liam Chen",
        "subjects": {
            "Mathematics": {"score": 92, "attendance": "98%", "notes": "Exceptional problem solver, helps peers understand concepts", "behavior": "Excellent"},
            "English": {"score": 75, "attendance": "85%", "notes": "Struggles with essay structure, improving vocabulary", "behavior": "Needs Improvement"},
            "Science": {"score": 88, "attendance": "94%", "notes": "Strong analytical skills, excellent lab reports", "behavior": "Excellent"},
            "History": {"score": 80, "attendance": "88%", "notes": "Good memory for dates, needs deeper analysis", "behavior": "Good"},
            "Art": {"score": 70, "attendance": "82%", "notes": "Technical skills developing, needs confidence", "behavior": "Needs Improvement"},
            "Physical Education": {"score": 85, "attendance": "92%", "notes": "Good coordination, respectful team member", "behavior": "Good"}
        }
    },
    {
        "name": "Sophia Adeleke",
        "subjects": {
            "Mathematics": {"score": 78, "attendance": "90%", "notes": "Working hard on fractions, shows perseverance", "behavior": "Good"},
            "English": {"score": 95, "attendance": "98%", "notes": "Outstanding reading comprehension, eloquent speaker", "behavior": "Excellent"},
            "Science": {"score": 86, "attendance": "93%", "notes": "Excellent hypothesizing skills, thorough documentation", "behavior": "Excellent"},
            "History": {"score": 91, "attendance": "96%", "notes": "Deep thinker, makes connections across topics", "behavior": "Excellent"},
            "Art": {"score": 89, "attendance": "94%", "notes": "Creative and expressive, strong color sense", "behavior": "Excellent"},
            "Physical Education": {"score": 80, "attendance": "87%", "notes": "Improving fitness, positive attitude toward challenges", "behavior": "Good"}
        }
    },
    {
        "name": "Noah Williams",
        "subjects": {
            "Mathematics": {"score": 68, "attendance": "78%", "notes": "Struggles with abstract concepts, needs extra support", "behavior": "Needs Improvement"},
            "English": {"score": 72, "attendance": "82%", "notes": "Basic comprehension solid, writing needs development", "behavior": "Needs Improvement"},
            "Science": {"score": 75, "attendance": "80%", "notes": "Engages in hands-on activities, theory is challenging", "behavior": "Good"},
            "History": {"score": 70, "attendance": "76%", "notes": "Memorization difficult, benefits from visual aids", "behavior": "Needs Improvement"},
            "Art": {"score": 94, "attendance": "96%", "notes": "Exceptionally talented, expressive and imaginative", "behavior": "Excellent"},
            "Physical Education": {"score": 88, "attendance": "92%", "notes": "Energetic and enthusiastic, follows instructions well", "behavior": "Excellent"}
        }
    },
    {
        "name": "Olivia Martinez",
        "subjects": {
            "Mathematics": {"score": 91, "attendance": "97%", "notes": "Quick mental math, excels in problem-solving challenges", "behavior": "Excellent"},
            "English": {"score": 87, "attendance": "93%", "notes": "Strong vocabulary, needs to slow down when writing", "behavior": "Good"},
            "Science": {"score": 93, "attendance": "98%", "notes": "Natural curiosity, asks insightful questions", "behavior": "Excellent"},
            "History": {"score": 85, "attendance": "91%", "notes": "Good analytical skills, connects past to present", "behavior": "Good"},
            "Art": {"score": 82, "attendance": "88%", "notes": "Developing personal style, experimenting with media", "behavior": "Good"},
            "Physical Education": {"score": 90, "attendance": "95%", "notes": "Competitive spirit, excellent sportsmanship", "behavior": "Excellent"}
        }
    },
    {
        "name": "Ava Thompson",
        "subjects": {
            "Mathematics": {"score": 84, "attendance": "91%", "notes": "Consistent effort, strong geometry skills", "behavior": "Good"},
            "English": {"score": 90, "attendance": "95%", "notes": "Loves reading, insightful literary analysis", "behavior": "Excellent"},
            "Science": {"score": 77, "attendance": "86%", "notes": "Theory strong, needs confidence in lab work", "behavior": "Good"},
            "History": {"score": 88, "attendance": "93%", "notes": "Excellent research skills, detailed presentations", "behavior": "Excellent"},
            "Art": {"score": 86, "attendance": "90%", "notes": "Thoughtful compositions, good attention to detail", "behavior": "Good"},
            "Physical Education": {"score": 79, "attendance": "84%", "notes": "Participates willingly, building stamina gradually", "behavior": "Good"}
        }
    },
    {
        "name": "Mason Davis",
        "subjects": {
            "Mathematics": {"score": 89, "attendance": "94%", "notes": "Logical thinker, excels at equations and formulas", "behavior": "Excellent"},
            "English": {"score": 81, "attendance": "88%", "notes": "Improving grammar, good oral presentations", "behavior": "Good"},
            "Science": {"score": 95, "attendance": "99%", "notes": "Top performer, passionate about experiments", "behavior": "Excellent"},
            "History": {"score": 83, "attendance": "89%", "notes": "Solid knowledge base, could expand perspectives", "behavior": "Good"},
            "Art": {"score": 75, "attendance": "83%", "notes": "Functional approach, less interest in creative aspects", "behavior": "Needs Improvement"},
            "Physical Education": {"score": 87, "attendance": "91%", "notes": "Good all-around athlete, team-oriented", "behavior": "Good"}
        }
    },
    {
        "name": "Isabella Garcia",
        "subjects": {
            "Mathematics": {"score": 73, "attendance": "84%", "notes": "Working through anxiety about tests, capable learner", "behavior": "Needs Improvement"},
            "English": {"score": 92, "attendance": "96%", "notes": "Beautiful prose, advanced vocabulary for age", "behavior": "Excellent"},
            "Science": {"score": 80, "attendance": "88%", "notes": "Careful observer, excellent note-taking habits", "behavior": "Good"},
            "History": {"score": 87, "attendance": "92%", "notes": "Empathetic understanding of historical figures", "behavior": "Excellent"},
            "Art": {"score": 96, "attendance": "98%", "notes": "Exceptionally creative, pursues projects independently", "behavior": "Excellent"},
            "Physical Education": {"score": 83, "attendance": "89%", "notes": "Enjoys dance and rhythmic activities especially", "behavior": "Good"}
        }
    }
]


def add_students_to_sheet(students_data=None, sheet_name="Students", clear_existing=False):
    """
    Add multiple students with all their subjects to Google Sheets.
    
    Args:
        students_data (list): List of student dictionaries (uses SAMPLE_STUDENTS if None)
        sheet_name (str): Name of the sheet tab
        clear_existing (bool): If True, clears existing data before adding
    
    Returns:
        int: Number of rows added
    """
    try:
        worksheet = get_sheet(sheet_id=settings.GOOGLE_SHEET_ID, sheet_name=sheet_name)
        
        # Use sample data if none provided
        if students_data is None:
            students_data = SAMPLE_STUDENTS
        
        # Prepare rows to add
        rows_to_add = []
        
        for student in students_data:
            name = student["name"]
            for subject, details in student["subjects"].items():
                row = [
                    name,
                    subject,
                    details["score"],
                    details["attendance"],
                    details["notes"],
                    details["behavior"]
                ]
                rows_to_add.append(row)
        
        if clear_existing:
            # Clear all data except headers
            worksheet.clear()
            # Add headers back
            headers = ["Name", "Subject", "Score", "Attendance", "Notes", "Behavior"]
            worksheet.update('A1:F1', [headers])
            start_row = 2
        else:
            # Find next empty row
            start_row = len(worksheet.col_values(1)) + 1
        
        # Batch update for efficiency
        end_row = start_row + len(rows_to_add) - 1
        range_notation = f'A{start_row}:F{end_row}'
        
        worksheet.update(range_notation, rows_to_add)
        
        logger.info(f"✅ Added {len(rows_to_add)} rows ({len(students_data)} students × {len(SUBJECTS)} subjects)")
        print(f"\n✅ Successfully added {len(students_data)} students with {len(rows_to_add)} total subject records!")
        print(f"📊 Range updated: {range_notation}")
        
        return len(rows_to_add)
    
    except Exception as e:
        logger.error(f"❌ Failed to add students: {e}")
        print(f"\n❌ Error: {e}")
        raise


def add_single_student(name, subject_scores, sheet_name="Students"):
    """
    Add a single student with custom subject data.
    
    Args:
        name (str): Student name
        subject_scores (dict): Dictionary mapping subjects to their details
            Example: {"Mathematics": {"score": 85, "attendance": "90%", "notes": "...", "behavior": "Good"}}
        sheet_name (str): Name of the sheet tab
    
    Returns:
        bool: True if successful
    """
    student_data = [{
        "name": name,
        "subjects": subject_scores
    }]
    
    try:
        add_students_to_sheet(student_data, sheet_name)
        return True
    except Exception:
        return False


def interactive_add_student():
    """
    Interactive CLI for adding a student with all subjects.
    """
    print("\n" + "="*60)
    print("📝 ADD NEW STUDENT - Interactive Mode")
    print("="*60 + "\n")
    
    name = input("Student Name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    subject_scores = {}
    
    print(f"\nEnter details for {name} across all {len(SUBJECTS)} subjects:")
    print("-" * 60)
    
    for subject in SUBJECTS:
        print(f"\n📚 {subject}:")
        
        # Score
        while True:
            try:
                score = int(input("  Score (0-100): "))
                if 0 <= score <= 100:
                    break
                print("  ⚠️  Score must be between 0 and 100")
            except ValueError:
                print("  ⚠️  Please enter a number")
        
        # Attendance
        attendance = input("  Attendance (e.g., 95%): ").strip()
        if not attendance.endswith('%'):
            attendance += '%'
        
        # Notes
        notes = input("  Notes: ").strip()
        if not notes:
            notes = "No additional notes"
        
        # Behavior
        print("  Behavior: 1) Excellent  2) Good  3) Needs Improvement")
        behavior_choice = input("  Choose (1-3): ").strip()
        behavior_map = {
            "1": "Excellent",
            "2": "Good", 
            "3": "Needs Improvement"
        }
        behavior = behavior_map.get(behavior_choice, "Good")
        
        subject_scores[subject] = {
            "score": score,
            "attendance": attendance,
            "notes": notes,
            "behavior": behavior
        }
    
    # Confirm before adding
    print("\n" + "="*60)
    print(f"Ready to add {name} with {len(subject_scores)} subjects")
    confirm = input("Proceed? (yes/no): ").strip().lower()
    
    if confirm in ['yes', 'y']:
        if add_single_student(name, subject_scores):
            print(f"\n✅ {name} added successfully!")
        else:
            print(f"\n❌ Failed to add {name}")
    else:
        print("\n❌ Cancelled")


if __name__ == "__main__":
    import sys
    
    print("\n" + "="*60)
    print("🎓 AI TEACHING ASSISTANT - Student Data Manager")
    print("="*60)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "sample":
            # Add sample students
            print("\n📋 Adding 8 sample students with 6 subjects each...")
            add_students_to_sheet()
        
        elif command == "clear":
            # Clear and re-add
            confirm = input("\n⚠️  This will CLEAR all existing data. Continue? (yes/no): ").strip().lower()
            if confirm in ['yes', 'y']:
                print("\n🗑️  Clearing existing data and adding fresh samples...")
                add_students_to_sheet(clear_existing=True)
            else:
                print("❌ Cancelled")
        
        elif command == "interactive":
            # Interactive mode
            interactive_add_student()
        
        else:
            print(f"\n❌ Unknown command: {command}")
            print("\nUsage:")
            print("  python add_students.py sample      - Add 8 sample students")
            print("  python add_students.py clear       - Clear sheet and add fresh samples")
            print("  python add_students.py interactive - Add student interactively")
    
    else:
        # Default: Add samples
        print("\n📋 No command specified. Adding sample students...")
        print("💡 Tip: Use 'python add_students.py interactive' for custom entry\n")
        add_students_to_sheet()
