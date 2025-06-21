import sys 
import os 
sys.path.append(os.getcwd())
from task.two import task2 as tk2
from task.one import task1 as tk1
def three():
    while(1):
        choice=int(input("enter your choice :"))
        if choice==1:
            tk1.onecalling()
        elif choice==2:
            tk2.twocalling()
        else:
            print("invalid !")
three()
 