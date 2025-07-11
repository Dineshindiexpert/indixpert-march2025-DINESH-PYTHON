list=[]
n=int(input("enter how many digit ascending :"))
for i in range(n):
    element=int(input("enter the element:"))
    list.append(element)
for i in list(n-1):
#     if list[i]>list[i+1]:
#         list[i],list[i+1]=list[i+1],list[i]
#     else:
#         print("no need to sort")
    
    print(list[i])    
    
