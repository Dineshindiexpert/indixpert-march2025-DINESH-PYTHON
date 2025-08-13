class studentmodel:
    def __init__(self):
        self.id=str
        self.name=str
        self.contact=str
        self.address=str

class inputdata:

    def registeredstudent(self):
        model=studentmodel()
        model.id=input("enter your id :")
        model.name=input("enter you name :")
        model.contact=input("enter you contact:")
        model.address=input("enter your address:")
    
        return model
    def dataprint(self,data):
        print("*"*100)
        print("here will be student data:-")
        print("student id:",data.id)
        print("student name :",data.name)
        print("student contact:-",data.contact)
        print()