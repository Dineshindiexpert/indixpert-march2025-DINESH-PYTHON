import json
import os

class Data:
    def __init__(self):
        
        if os.path.exists("format.json"):
            with open("format.json", "r") as file:
                self.studentdata = json.load(file)
        else:
            self.studentdata = []

    def registration(self):
        student = {}
        student["id"] = input("Enter your ID: ")             
        student["name"] = input("Enter your name: ")
        student["contact"] = input("Enter your contact number: ")
        student["gmail"] = input("Enter your Gmail: ")
        self.studentdata.append(student)

    def write(self):
        with open("format.json", "w") as file:
            json.dump(self.studentdata, file, indent=4)

    def display(self):
        for student in self.studentdata:
            print(student)


student = Data()
student.registration()
student.write()
student.display()
