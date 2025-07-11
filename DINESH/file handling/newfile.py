import json
import os
import datetime

def createregisteration():
    with open("data.json", "r") as f:
        content = f.read()
        data = json.loads(content)

    makefile = int(input("How many student register  the add: "))
    with open("data.txt", "a") as textdata:
        for i in range(makefile):
            studentdata = {}
            studentdata["id"] = input("Enter student ID: ")
            studentdata["studentname"] = input("Enter student name: ")
            registrationdate = str(datetime.datetime.now().date())
            studentdata["registered date"] = registrationdate
            data.append(studentdata)
            textdata.write(f"{registrationdate} - {studentdata['studentname']}\n")
    with open("data.json", "w") as jsondata:
        jsondata.write(json.dumps(data, indent=4))
    print("Registered successfully.")

def readfile():
    with open("data.json", "r") as jsonfile:
        content = jsonfile.read()
        data = json.loads(content)
        print("Registered Students:")
        for student in data:
            print(f"ID: {student['id']}, Name: {student['studentname']}")
        return data
        
def searchdata():
    userid = input("Enter the user ID to search: ")
    with open("data.json", "r") as jsonfile:
        content = jsonfile.read()
        data = json.loads(content)
        flag = 0
        for student in data:
            if student["id"] == userid:
                print("Data found!")
                print(f"ID: {student['id']}, Name: {student['studentname']}")
                flag = 1
                break
            if flag == 0:
                print("Data not found!")
             
def menu():
    while True:
        print(" MENU ")
        print("1. Register students")
        print("2. Show all students")
        print("3. Search student by ID")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            createregisteration()
        elif choice == '2':
            readfile()
        elif choice == '3':
            searchdata()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
