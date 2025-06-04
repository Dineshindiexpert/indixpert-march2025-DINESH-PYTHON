# studentdetails={"name":"dinesh","age":"18","father":"rihsipal","adress":"rohtak","state":"haryana",}

# studentdetails.pop("state")
# print(studentdetails)
# for key,value in studentdetails.items():
#     print(f"{key}={value}")

# print(studentdetails.items())
num1=int(input("enter your first number :"))
num2=int(input("enter your second number :"))
calculator={"sum":num1+num2,"subtract":num1-num2,"multipy":num1*num2,"divide":num1/num2}
print("                                     HERE YOUR CALCULATOR")
print("#"*150)
for i,j in calculator.items():
    print(f"#                                   {i} = {j}                                                ")