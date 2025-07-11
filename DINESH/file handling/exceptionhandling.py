import datetime
import os
import json


path = r"C:\Users\jai seya ram\OneDrive\Documents\project indiexpert"
file = datetime.datetime.now().date()
extension = ".txt"
finalfile = str(file) + extension
finalpath = os.path.join(path, finalfile)

try:
    student_list = []
    with open(finalpath, "w") as file:
        studentdata = {}
        studentdata["studentpin database"] = "1234"

        try:
            studentdata["student name"] = input("Enter the student name: ")
            studentdata["student pin"] = int(input("Enter the student pin: "))

            
            if str(studentdata["student pin"]) == studentdata["studentpin database"]:
                print("PIN match successful.")
            else:
                print("PIN mismatch.")

            time = datetime.datetime.now()
            student_list.append(studentdata)

        except Exception as file_error:
            time = datetime.datetime.now()
            with open("data.txt", "a") as datafile:  
                datacontent =(
                    f"[{time}] Exception for student '{studentdata.get('student name', 'Unknown')}': "
                    f"{file_error}\n")
                datafile.write(datacontent)

        file.write(json.dumps(student_list, indent=4))
        print("File created successfully!")

except Exception as error:
    time = datetime.datetime.now()
    with open("data.txt", "a") as err_file:  
        statement = f"[{time}] Outer exception: {error}\n"
        space="     \n"
        err_file.write(space)
        err_file.write(statement)
