class StudentModel:
    def __init__(self):
        self.id = str
        self.name = str
        self.address = str
        self.pincode = str

class Main:

    def getinput(self):
        regis = StudentModel()
        regis.id = input("Enter your ID: ")
        regis.name = input("Enter your Name: ")
        regis.address = input("Enter your Address: ")
        regis.pincode = input("Enter your Pincode: ")

        return regis


    def dataprint(self, data):
        print("#" * 50)
        print("Student data will be:")
        print("Student ID:", data.id)
        print("Student Name:", data.name)
        print("Student Address:", data.address)
        print("Student Pincode:", data.pincode)




ob=Main()
output=ob.getinput()
ob.dataprint(output)

    


