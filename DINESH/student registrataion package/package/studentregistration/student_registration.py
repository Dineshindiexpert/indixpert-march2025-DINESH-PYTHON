from package.studentdashboard import student_dashboard as dashboard
def studentregistration():
    studentdata = []

    dashboard.menu()

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
            print(f"\nRegistering student: {i + 1}")
            student = {}

            student["id"] = input("Enter student ID: ")

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
                countrycode = input("Enter the country code: ")
                if countrycode.isdigit():
                    break
                else:
                    print("Invalid country code! Must be numeric.")

            while True:
                contact = input("Enter student contact number: ")
                if contact.isdigit() and len(contact) >= 10:
                    student["contact"] = f"{countrycode}+{contact}"
                    break
                else:
                    print("Invalid contact number! Must be at least 10 digits.")

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
                            subqualification["passing year"] = year
                            break
                        else:
                            print("Invalid year! Must be a number.")
                    qualification.append(subqualification)
                else:
                    print("Invalid input! Please type 'yes' or 'no'.")

            student["qualification"] = qualification
            studentdata.append(student)
        break

    return studentdata
