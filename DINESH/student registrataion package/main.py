from package.studentmenu.student_menu import show_main_menu, get_user_choice
from package.studentregistration.student_registration import studentregistration
from package.studentsearch.student_search import search_students
from package.studentdisplay.student_display import display_students
from package.database.database import add_students, get_all_students

def main():
    print("Welcome to Student Management System ")

    while True:
        show_main_menu()
        choice = get_user_choice()

        if choice == 1:
            students = studentregistration()
            add_students(students)

        elif choice == 2:
            display_students(get_all_students())

        elif choice == 3:
            search_students(get_all_students())

        elif choice == 4:
            print(" thanks")
            break

if __name__ == "__main__":
    main()
