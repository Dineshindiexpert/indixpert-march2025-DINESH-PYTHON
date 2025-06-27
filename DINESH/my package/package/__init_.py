import datetime
import json
listdata = []
for n in range(1, 4):
    dictdata = {}
    dictdata["id"] = input("Please enter student id: ")
    dictdata["name"] = input("Please enter student name: ")
    dictdata["address"] = input("Please enter address: ")
    if n < 3:
        dictdata["createddate"] = str(datetime.datetime.now().date())
    else:
        dictdata["createddate"] = str(datetime.datetime.now().date() + datetime.timedelta(days=2))
    
    listdata.append(dictdata)
print(json.dumps(listdata, indent=4))


date = input("Enter a date  : ")
flag=0
for i in listdata:
    if i["createddate"]==date:
        flag =1
 
        for key, value in i.items():
            print(json.dumps(f"{key} = {value}"))

if  flag==0:
    print("Data not found!")
 