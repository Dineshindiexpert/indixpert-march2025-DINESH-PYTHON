print("HEY. THIS IS THE EXCELLENT SOFTWEARE. PLEASE ENTER THE ALL NECRSSAARY DETAILS.")

while (1):
    
    studentname=input("enter to person to make data :")
    NAME=input("ENTER YOUR NAME:")

    age=input("enter your age:")
    religion=input("enter your religion:")
    maritalstatus=input("are you maried ? :")
    current =input("enter what you work in present :")
    adress=input("enter your address :")
    state=input("enter your state :")
    father=input("enter your father name:")
    contact=input("enter your CONTACT :")
    alternatecontact=input("enter your alternate contact number:")
    gmail=input("enter your gmail:")
    experience=input("enter your work experinece :")
    country=input("enter your country:")
    MATRIX=input("IF YOU PASS 10 CLASS ?:")
    FROM=input("where you from pass class 10th :")
    class10from=input("adress of school:")
    tweleth=input("are you passed 12 class :")
    class12from=input("address of school:")
    from2=input("where you passed class 12th:")


    # print("#"*135)
    # dinesh={"NAME":"DINESH","age":"18","religion":"HINDU","MARITAL STATUS":"UNMARRIED","WORKING ON":"FULL STACK DEV","ADRESS":"ROHTAK","STATE":"HARYANA","FATHER":"RISHIPAL","CONTACT":"9896*****","ALTERNATE":"95186***** ","GMAIL":"DINSEHJANGRA0062@GMAIL.COM","EXPERCIENCE":"0YEARS","COUNTRY":"INDIA",}
    # print("#                                                     ***** DINESH DETAILS *****                                                                                         ")
    # for key, value in dinesh.items():
    #     print(f"#                                                         {key} = {value}                                                                                 ")

    # print("#"*145)
    print()
    print()

        
    # print("#"*60,"QUALIFICATIONS.","#"*68)
    # qualifications={"10TH":"Jawahar Navodaya Vidyalaya","From":"Rohtak","12th":"Jawahar Navodaya Vidyalaya",}
    # print("#")
    # for key,value in qualifications.items():
    #     print(f"#                                                           {key} = {value}                                                                                 ")
        
    # print("#")
    # print("#"*145)
    print("#"*135)
    dinesh={"NAME":NAME,"age":age,"religion":religion,"MARITAL STATUS":maritalstatus,"WORKING ON":current,"ADRESS":adress,"STATE":state,"FATHER":father,"CONTACT":contact,"ALTERNATE":alternatecontact,"GMAIL":gmail,"EXPERCIENCE":experience,"COUNTRY":country,}
    print(f"#                                                    ***** {studentname}, DETAILS *****                                                                                         ")
    for key, value in dinesh.items():
        print(f"#                                                         {key} = {value}                                                                                 ")

    print("#"*145)

    print()
    print(f"#"*135)
    print(f"#                                                          {studentname}  QUALIFICATIONS"," "*68)
    qualifications={"10TH":MATRIX,"From":class10from,"12th":tweleth,"from":class12from,"adress":from2}
    print("#")
    for key,value in qualifications.items():
        print(f"*                                                            {key} = {value}                                                                                 ")
        
    print("#"*135)
    while(1):
        choice=input("do you conatinue another response (yes/no)? :")
        if choice=="no":
            break
        elif choice=="yes" :
            print("continue") 
            break
        else:
            print("invalid choice")
    