def login_window():
    username = "abc123"
    password = "abc@123"
    while True:
        user = input("Enter the username: ")
        passwd = input("Enter the password : ")
        if user == username and passwd == password:
            print("Successfully login")
            break
        else:
            print("Invalid ID or password! Please try again.")
def menu():
    print(f"{'....MENU....'}")
    print("""
    1. Register student
    2. Display student data
    3. Search student
    4. Exit
    """)
def student_registration():
    studentdata=[]
    while True:
        num = input("Enter how many students to register (1 to 10): ")
        if not num.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        num = int(num)
        if num < 1 or num > 10:
            print("Invalid! Please enter a number between 1 and 10.")
            continue

        for i in range(num):
            print(f"Registering student: {i + 1}")
            student = {}

            while True:
                student_id = input("Enter student ID: ")
                if student_id.isalnum():
                    student["id"] = student_id
                    break
                else:
                    print("Invalid ID! Use letters or digits only.")

            while True:
                name = input("Enter student name: ")
                if name.isalpha():
                    student["name"] = name
                    break
                else:
                    print("Invalid name! Please use only alphabets.")

            while True:
                address = input("Enter student address: ")
                if address.isalnum():
                    student["address"] = address
                    break
                else:
                    print("Invalid address! Use alphanumeric characters only.")

            while True:
                countrycode = input("Enter the country code (e.g., 91): ")
                if countrycode.isdigit() and len(countrycode) == 2:
                    break
                else:
                    print("Invalid country code! Must be 2 digits.")

            while True:
                contact = input("Enter contact number: ")
                if contact.isdigit() and len(contact) >= 10:
                    student["contact"] = contact
                    break
                else:
                    print("Invalid contact number! At least 10 digits.")

            qualification = []
            while True:
                choice = input("Do you want to add a qualification? (yes/no): ").lower()
                if choice == "no":
                    break
                elif choice == "yes":
                    subqualification = {}
                    subqualification["name"] = input("Enter qualification name: ")
                    while True:
                        year = input("Enter passing year: ")
                        if year.isdigit():
                            subqualification["passing year"] = int(year)
                            break
                        else:
                            print("Invalid year!")
                    qualification.append(subqualification)
                else:
                    print("Please enter 'yes' or 'no'.")

            student["qualification"] = qualification
            studentdata.append(student)
        break
    return studentdata

def display_student(studentdata):
    print("-" * 100)
    print(" " * 30 + "................. Student Data .................")
    print("-" * 100)

    if not studentdata:
        print("                       NO data availabe here ")
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
    return studentdata

def student_search(studentdata):
    if not studentdata:
        print("No student data available. Please register students first.")
        return studentdata

    print("""
    --- Search Student ---
    1. Search by Name
    2. Search by ID
    3. Search by Contact
    4. Exit Search
    """)
    while True:
        choice = input("Enter your choice to search: ")

        if choice == "1":
            name = input("Enter name to search: ").lower()
            found = False
            for student in studentdata:
                for key, value in student.items():
                    if key == "qualification":
                        print(f"{key}:")
                        for i in value:
                            print("    ", i)
                    else:
                        print(f"{key}: {value}")
                    
            found = True
            if not found:
                print("No student found with that name.")

        elif choice == "2":
            sid = input("Enter name to search: ").lower()
            found = False
            for sid in studentdata:
                for key, value in student.items():
                    if key == "qualification":
                        print(f"{key}:")
                        for i in value:
                            print("    ", i)
                    else:
                        print(f"{key}: {value}")
        elif choice == "3":
            while True :
                contact = input("Enter contact to search: ")
                if len(contact)==10 and contact.isdigit() and int(contact):
                    print("\n valid contact "^50)
                    print("processing"^50)
                    break
                else:
                    print("invalid contact ! TRY AGIAN "^50)
            found = False
            for student in studentdata:
                if contact in student["contact"]:
                    print("Student Found:")
                    print(student)
                    found = True
            if not found:
                print("No student found with that contact."^50)

        elif choice == "4":
            print("Exiting search."^50)
            break
        else:
            print("Invalid option!")
    return studentdata

def choice():
    login_window()
    studentdata = []  

    while True:
        menu()
        option = input("Enter your option: ")
        if option == "1":
            new_data = student_registration()
            if new_data:
                studentdata.extend(new_data)
        elif option == "2":
            display_student(studentdata)
        elif option == "3":
            student_search(studentdata)
        elif option == "4":
            print("Thank you. Exiting...")
            break
        else:
            print("Invalid option! Please choose between 1 to 4.")
    return studentdata




choice()
