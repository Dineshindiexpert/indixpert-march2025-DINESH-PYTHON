# start 
print(""" menu given below.
      1. for the sum
      2. for the subtract 
      3. for the multiply
      4. for the division """)
num1=int(input("enter first number:"))
num2=int(input("enter your second number:"))
choice=int(input("enter your choice:"))


if choice==1:
    print("sum")
    
    print(num1+num2)
elif choice==2:
    print("subtract")
    
    print(num1-num2)
elif choice==3:
    print("multiply")
    
    print(num1*num2)
elif choice==4:
    print("division")
    
    print(num1/num2)
else:
    print("invalid")