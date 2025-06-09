print("""
         WELCOME TO RESULT SOFTWARE
     This is a totally user-friendly software.
         OK, Let's enjoy!
""")
password="abc@123"
while(1):
    userpassword=input("enter to password to access your software :")
    print("congraltions.!")
    if userpassword==password:
        id = int(input("Enter the student ID: "))
        name = input("Enter the student name: ")
        namef=name.capitalize()
        contact = input("Enter the student contact: ")
        address = input("Enter the student address: ")
        addressf=address.capitalize()


        print("\nOK, ENTER THE STUDENT MARKS.")
        print()
        hindi = int(input("HINDI MARKS: "))
        eng = int(input("ENGLISH MARKS: "))
        math = int(input("MATH MARKS: "))
        sci = int(input("SCIENCE MARKS: "))



        TOTAL = hindi + eng + math + sci
        percentage = (TOTAL / 400) * 100  

        if percentage>=35:
            status="PASS."
        else:
            status="fail !"



        print("#"*100)

        print("""                                   ...............student report....................                                                           """)
        print(f""" 
                                                                ID       : {id}
                                                                NAME     : {namef}
                                                                CONTACT  : {contact}
                                                                ADDRESS  : {addressf}
        """)
        print("."*100)
        print(f"                                                 {namef} MARKS ")

        print(f"""
            HINDI    : {hindi}
            ENGLISH  : {eng}
            MATH     : {math}
            SCIENCE  : {sci}
            TOTAL    : {TOTAL}
            PERCENT  : {percentage}%
            STATUS   : {status}
        """)
        print("#"*100)
        break
    else:
        print("""invalid password  
                try again 
              """)
    
        
    
