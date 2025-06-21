print("""
         WELCOME TO RESULT SOFTWARE
     This is a totally user-friendly software.
         OK, Let's enjoy!
""")

id = int(input("Enter the student ID: "))
name = input("Enter the student name: ")
contact = input("Enter the student contact: ")
address = input("Enter the student address: ")


print("\nOK, ENTER THE STUDENT MARKS.")
print()
hindi = int(input("HINDI MARKS: "))
eng = int(input("ENGLISH MARKS: "))
math = int(input("MATH MARKS: "))
sci = int(input("SCIENCE MARKS: "))



TOTAL = hindi + eng + math + sci
percentage = (TOTAL / 400) * 100  

if percentage>=35:
    status="fail."
else:
    staus="fail"



print("#"*100)

print("""                                   ...............student report....................                                                           """)
print(f""" 
                                                        ID       : {id}
                                                        NAME     : {name}
                                                        CONTACT  : {contact}
                                                        ADDRESS  : {address}
""")
print("."*100)
print(f"                                                 {name} MARKS ")

print(f"""
    HINDI    : {hindi}
    ENGLISH  : {eng}
    MATH     : {math}
    SCIENCE  : {sci}
    TOTAL    : {TOTAL}
    PERCENT  : {percentage:.2f}%
    STATUS   : {print(status)}
""")
print("#"*100)
