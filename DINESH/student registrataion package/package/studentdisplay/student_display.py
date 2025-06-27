from package.studentregistration import student_registration as reg

from package.database.database import get_all_students

all_students = get_all_students()



def display_students(studentdata):
    if not studentdata:
        print("No student data to display.")
        return

    print("=" * 100)
    print(" " * 30 + "All Registered Students")
    print("=" * 100)
    
    count = 1  

    for student in studentdata:
        print(f"Student {count}")
        print("-" * 50)
        for key, value in student.items():
            if key == "qualification":
                print("Qualifications:")
                for i in value:
                    print(f"  - {i['name']} ({i['passing year']})")
            else:
                print(f"{key}: {value}")
        count += 1
