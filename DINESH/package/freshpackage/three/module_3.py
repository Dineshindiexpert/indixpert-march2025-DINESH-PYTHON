from freshpackage.one import module_1 as mod1
from freshpackage.two import module_2 as mod2
print("third module is calling.")
def callmain():
    
    while True:
        choice=int(input("enter your choice :"))
        if choice==1:
            print("thanks module 1.")
            mod1.printmodule1
            break
        elif choice==2:
            print("thanks.")
            mod2.printmodule_2
            print("module 2 is calling.")
            break
        else:
            print("invalid !")
callmain()
