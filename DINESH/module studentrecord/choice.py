import studentregistration as registration
import menu
import studentdisplay as display
import studentsearch as search
import choice

def choice():
    studentdata=[] 
    

    while True:
        menu.menu()
        option = input("Enter your option: ")
        if option == "1":
            new_data = registration.student_registration()
            
            
            
            if new_data:
                studentdata.extend(new_data)
        elif option == "2":
            display.display_student(studentdata)
        elif option == "3":
            search.student_search(studentdata)
        elif option == "4":
            print("Thank you. Exiting...")
            break
        else:
            print("Invalid option! Please choose between 1 to 4.")
    return studentdata

