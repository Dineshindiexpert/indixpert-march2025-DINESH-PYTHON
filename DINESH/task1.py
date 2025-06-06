id=int(input("enter your id :"))
name=input("emter your name :")
if name.isdigit():
    print("invalid please valid name!")
address=input("enter your address:")
while(1):
    hindi=(input("please enter the hindi marks :"))
    if hindi.isdigit():
        print("continue")
    else:
        print("invalid")
        break

english=int(input("please enter the englis marks:"))
math=int(input("please enter the math marks:"))
science=int(input("please enter the science marks:"))
print(""" student record
       """)
print(f"studend id :{id}")
print(f"name :{name}")
print(f"address:{address}")
print(f"hindi marks :{hindi}")
print(f"english:{english}")
print(f"math:{math}")
print(f"science :{science}")
print(f"student total marks obtained:{hindi+english+math+science}")
print(f"student percentage:{((hindi+english+math+science)%400)*100}")

