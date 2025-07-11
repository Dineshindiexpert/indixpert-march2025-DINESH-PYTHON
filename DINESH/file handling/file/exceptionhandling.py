import json
def studentregistration():
    with open("resgister.json","w") as file:
        student={}
        content=student["id"]=input("ENTER ID HERE :")
        file.write(json.dumps(content))
studentregistration()
