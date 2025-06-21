# start 
print(""" menu given below
      a. for  the sum'
      s. fot the subtract
      m. for the multiply
      d. for the division""")
num1=int(input("enter first number:"))
num2=int(input("enter your second number:"))
choice=(input("enter your choice:"))
final= choice.lower()

if final=="a":
    print("sum")
    
    print(num1+num2)
elif final=="s":
    print("subtract")
    
    print(num1-num2)
elif final=="m":
    print("multiply")
    
    print(num1*num2)
elif final=="d":
    print("division")
    
    print(num1/num2)
else:
    print("invalid")