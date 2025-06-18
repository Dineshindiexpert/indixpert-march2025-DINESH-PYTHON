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
