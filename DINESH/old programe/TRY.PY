id=int(input("enter your id :"))
name=input("enter your name:")
contact=input("enter your contact no:")
address=input("enter your address")
qualification1=input("enter qualification:")
passing1=input("enter passing year:")
qualification2=input("enter qualification:")
passing2=input("enter passing year :")
id=int(input("enter your id :"))
name=input("enter your name:")
contact=input("enter your contact no:")
address=input("enter your address")
qualification1=input("enter qualification:")
passing1=input("enter passing year:")
qualification2=input("enter qualification:")
passing2=input("enter passing year :")
student=[{"id":id,"name":name,"contact":contact,"ADDRESS":address},{"id":id,"name":name,"contact":contact,"address":address},{"qualification":qualification1,"passing year":passing1,"qualification2":qualification2,"passing year ":passing2},{"qualification":qualification1,"passing year":passing1,"qualification2":qualification2,"passing year":passing2}]
print("""                                               MENU
                                                    1.PRESS FOR THE ID 
                                                    2. PRESS FOR THE QUALIFICATION """)
while True:
    choice=int(input("enter your choice:"))
    if choice==1:
        print("ok your data.")
        print(student[0].items)
        print(student[1].items)

        break
    elif choice==2:
        print("ok qualification.")
        print(student[2].items())
        print(student[3].items())
        break
    else:
        print("invalid choice!.")
