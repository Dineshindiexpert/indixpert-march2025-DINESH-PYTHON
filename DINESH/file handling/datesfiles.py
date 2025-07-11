import datetime
import os
path=r"C:\Users\jai seya ram\OneDrive\Documents\project indiexpert"
file=datetime.datetime.now().date()
extension=".txt"
finalfile=str(file)+extension
finalpath=os.path.join(path, finalfile)
if os.path.exists(finalpath):
    print("hey user your file is also created !")
else:
    with open(finalpath,"x") as file:
        content="hey user !"
        file.write(content)
        print("file created sucessfully now !")





     