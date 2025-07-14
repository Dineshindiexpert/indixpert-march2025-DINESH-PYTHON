
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
      num=int(input("enter how many student input:"))  
      if num<0 and num>10:
        print("invalid")
      else:
        for i in range(num):
            student={}
            student["id"]=int(input("enter the student id :"))
            student["name"]=input("enter the student name :")
            student["address"]=input("enter the student address:")
            student["contact"]=input("enter the studetn contact number:")
            qualification=[]
            count=1
            while(True):
                choice=input("do you want to add qualification (yes/no):")
                choice.lower()
                if choice=="yes":
                
                     subqualification={}
                     subqualification["name "]=input("enter the qualification name :")
                     subqualification["passing year"]=int(input("enter the passing year "))
                     qualification.append(subqualification)
                
                elif choice=="no":
                     print("thanks ")
                    
            
                else:
                    print("invalid !")
                student["qualification"]=qualification
                studentdata.append(student)

        break
     





print("""           ...........qualification...........                   """) 
for items in studentdata:
    for key,values in items.items(4):
        print(f"  {key} =   {values}")
         

        
         
        
 




             


        
         
        
 


