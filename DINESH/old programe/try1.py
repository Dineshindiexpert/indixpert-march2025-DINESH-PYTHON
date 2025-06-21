studentrecord = []
while(1):
    username=input("enter username :")
    password=input("enter your passsword :")

    if username=="abc" and password=="abc@123":
        print("successfully login")
        break
    else:
        print("invalid !")

count=1
for i  in range(5):
    id = int(input(f"Enter the student ID {count}: "))
    name = input(f"Enter the student name {count}: ")
    address = input(f"Enter the student address {count}: ")
    

    studentdata =[{
            "id": id,
            "name": name,
            "address": address}]
    print("                                   qualification:")
    
    
    while(1):
        
        qualification=input("enter qualification :")
        year=input("enter the passing year :")
        studentdataq={
            "qualification":qualification,
            "passing year":year
        }
        qualificationmore=input("have another qualification :yes 0r no :")
        if qualificationmore=="no":
            studentdata.appent(qualification)


        
            

    studentrecord.append(studentdata)
    count=count+1
    # while(1): 
    #     choice = input("Do you want to add more student data? (yes/no): ")
    #     choicef=choice.lower() 
    #     if choicef == "yes":
    #         print("Thanks!")
    #         break
    #     elif choicef == "no":
    #         print(" ok continue")
    #         continue
    #     else:
    #         print("""invalid id or password!
    #             try again !""")
            
    
        
        

print("#" * 100)
print("""                                                                  OUTPUT                                                                   """)
print("#" * 100)
start=1
for items in studentrecord:
    for key,values in items.items():
        print(f" {key} = {values}")
    print("-"*50)
    print(f"NO OF STUDENT DATA = {count}:")
    start+=start
