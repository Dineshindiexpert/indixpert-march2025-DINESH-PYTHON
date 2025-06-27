from package.database import database as db

def search_students(studentdata):
    if not studentdata:
        print("No student data available to search.")
        return

    while True:
        print("====== SEARCH MENU ======")
        print("1. Search by Name")
        print("2. Search by Contact")
        print("3. Search by Qualification")
        print("4. Exit Search")
        

        
        choice = int(input("Enter your choice (1-4): "))
         
        if choice == 1:
            name = input("Enter student name to search: ")
            name.strip().lower()
            flag = 0
            for student in studentdata:
                if student.get("name", "").lower() == name:
                    print_student(student)
                    flag = 1
            if  flag==0:
                print(" No student found with that name.")

        elif choice == 2:
            contact = input("Enter contact no (with country code, e.g., 91+9876543210): ")
            contact.strip()
            flag= 0
            for student in studentdata:
                if student.get("contact", "") == contact:
                    print_student(student)
                    flag = 1
            if  flag==0:
                print(" No student found with that contact number.")

        elif choice == 3:
            qname = input("Enter qualification name to search: ")
            qname.strip().lower()
            flag = 0
            for n in studentdata:
                for y in n["qualification"]:
                    for key,value in y.items():
                        if value==qname:
                            print(n)
            for i in studentdata():
                if student.get("qualification", [])==qname :
                    print()




            # for key, value in student.items():
            #     if key == "qualification":
            #         print("Qualifications:")
            #         for key1,value1 in key:
                         
            #     else:
            #         print(f"{key}: {value}")
            if flag==0:
                    print("No student found with that qualification.")

        elif choice == 4:
            print("Exiting search menu.")
            break

        else:
            print("Invalid choice! Please select between 1 to 4.")

def print_student(student):
    print("-" * 50)
    for key, value in student.items():
        if key == "qualification":
            print("Qualifications:")
            for i in value:
                print(f"  {i[' qualification name']} ({i['passing year']})")
        else:
            print(f"{key}: {value}")
    print("-" * 50)
