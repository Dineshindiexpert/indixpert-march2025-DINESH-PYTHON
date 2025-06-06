# num=int(input("       enter your number:"))
# print()
# if num%2==0:
#     print(f"       {num}  is even number.")
# else:
#     print(f"       {num} is  odd number.")
# print()
# print("         thanks. !")
print("""   menu given below
      a. press for the sum
      s. press for the subtract
      m. press for the multiply
      d. pesss for the division 
      """)

num1=int(input("enter first number:"))
num2=int(input("enter your second number:"))
choice=(input("enter your choice:"))
if choice=="a":
    print("sum")
    print(num1+num2)
elif choice=="s":
    print("subtract")
    print(num1-num2)
elif choice=="m":
    print("multiply")
    print(num1*num2)
elif choice=="d":
    print("division")
    print(num1/num2)
else:
    print("invalid")