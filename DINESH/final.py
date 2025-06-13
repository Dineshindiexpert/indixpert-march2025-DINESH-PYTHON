def login_window():
    username="abc123"
    password="abc@123"
    while True:
        user=input("                                               enter the username:")
        passwd=input("                                             enter the password :")
        if user==username and passwd==password:
            print("                                                sucessfully login")
            break
        else:
            print("                                                Invalid ID or password! Please try again.")
def menu():
    
    print(f"                                                                ....MENU....")
    print("""
                                                                        1. Register student
                                                                        2. Display student data
                                                                        3. Search student
                                                                        4. Exit
                                                                            """)
studentdata = []
def student_registration():
    while True:
        num = input("                                           Enter how many students to register (1 to 10): ")
        
        if not num.isdigit():
            print("                                             Invalid input! Please enter a number.")
            continue

        num = int(num)
        if num < 1 or num > 10:
            print("                                             Invalid! Please enter a number between 1 and 10.")
            continue
         


        
                 


        for i in range(num):
            print(f"                                            Registering student: {i + 1}")
            student = {}

            while True:
                student_id = input("                            Enter student ID: ")
                if not student_id.isalnum():
                    print("                                     Invalid ID! Use letters or digits only.")
                else:
                    student["id"] = student_id
                    break

            while True:
                name = input("                                  Enter student name: ")
                if  name.isalpha():
                    student["name"] = name
                    break
                else:
                    print("                                     Invalid name! Please use only alphabets.")

            while True:
                address = input("                               Enter student address: ")
                if address.isalnum():
                    student["address"] = address
                    break
                else:
                    print("                                     Invalid address! Use alphanumeric characters only.")

            while True: 
                countrycode = input("                           Enter the country code (e.g., 91): ")
                if countrycode.isdigit() and len(countrycode) == 2:
                    break
                else:
                    print("                                     Invalid country code! Must be 2 digits.")

            while True:
                contact = input("                               Enter contact number: ")
                if len(contact) >= 10 and contact.isdigit():
                    student["contact"] = contact
                    break
                else:
                    print("                                     Invalid contact number! At least 10 digits.")

            qualification = []
            while True:
                choice = input("                                Do you want to add a qualification? (yes/no): ").lower()
                if choice == "no":
                    break
                elif choice == "yes":
                    subqualification = {}
                    subqualification["name"] = input("         Enter qualification name: ")
                    while True:
                        year = input("                         Enter passing year: ")
                        if year.isdigit():
                            subqualification["passing year"] = int(year)
                            break
                        else:
                            print("                            Invalid year!")
                    qualification.append(subqualification)
                else:
                    print("                                    Please enter 'yes' or 'no'.")

            student["qualification"] = qualification
            studentdata.append(student)
        break
def display_student():
    print("-" * 100)
    print(" " * 30 + "................. Student Data .................")
    print("-" * 100)

    if not studentdata:
        print(" " * 40 + "No student data available.")
        print("-" * 100)
        return

    for student in studentdata:
        for key, value in student.items():
            if key == "qualification":
                print(f"{key}:")
                for i in value:
                    print("    ", i)
            else:
                print(f"{key}: {value}")
        print("-" * 100)
def student_search():
    print("""
                                                            --- Search Student ---
                                                            1. Search by Name
                                                            2. Search by ID
                                                            3. Search by Contact
                                                            4. Exit Search
    """)
    while True:
        choice = input("                                         Enter your choice to search: ")

        if choice == "1":
            name = input("                                       Enter name to search: ").lower()
            flag = 0
            for student in studentdata:
                if student["name"].lower() == name:
                    print("Student Found:")
                    print(student)
                    flag = 1
            if flag==0:
                print("                                         No student found with that name.")

        elif choice == "2":
            sid = input("                                       Enter ID to search: ")
            flag = 0
            for student in studentdata:
                if student["id"] == sid:
                    print("                                     Student Found:")
                    print(student)
                    flag = 1
            if flag==0:
                print("                                         No student found with that ID.")

        elif choice == "3":
            contact = input("                                   Enter contact to search: ")
            flag = 0
            for student in studentdata:
                if contact in student["contact"]:
                    print("                                     Student Found:")
                    print(student)
                    flag = 1
            if flag==0:
                print("                                         No student found with that contact.")

        elif choice == "4":
            print("                                             Exiting search.")
            break
        else:
            print("                                             Invalid option!")
def choice():

    while True:
        login_window()
        menu()
        while True:
            option = input("                                        Enter your option: ")
            if option == "1":
                student_registration()
            elif option == "2":
                display_student()
            elif option == "3":
                student_search()
            elif option == "4":
                print("                                             Thank you. Exiting...")
                break
            else:
                print("                                             Invalid option! Please choose between 1 to 4.")
choice()
