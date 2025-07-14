
while(1):
    username=input("enter the username :")
    password=input("enter the password :")
    if username=="abc" and password=="abc":
        print("successfuly login !")
        break
    else:
        print("invalid password!")


studentdata=[]

while(True):
    studentchoice=input("do you want to add student :")
    studentchoice.lower()
    if studentchoice=="yes":

        student={}
        student["id"]=int(input("enter the student id :"))
        student["name"]=input("enter the student name :")
        student["address"]=input("enter the student address:")
        student["contact"]=input("enter the studetn contact number:")
        qualification=[]
        while(True):
            choice=input("do you want to add qualification (yes/no):")
            choice.lower()
            if choice=="yes":

                subqualificatio={}
                subqualificatio["name "]=input("enter the qualification name :")
                subqualificatio["passing year"]=int(input("enter the passing year "))
                qualification.append(subqualificatio)
            else:
                break
        student.append(qualification)
        student.append(studentdata)
    else:
        break





print("""           ...........qualification.....                   """) 
print(studentdata)
        
 


