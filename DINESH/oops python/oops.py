import json
class data:
    def __init__(self):
        pass
    
     
                                   
    def registration(self):
        self.dict={}
        self.dict['id']=input("enter your id :")
        self.dict['name']=input("enter your name:")
        return self.dict
    def write(self):
        with open('format.json',"a") as file:
            file.write(json.dumps(self.dict,indent=4))
    def read(self):
        with open("format.json","r") as file:
           studentdata= file.read()
           print(studentdata)



student= data()
student.registration()
student.write()
student.read()