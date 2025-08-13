class full:
    def __init__(self):
        print("account holder : dinesh")
        print("account balance:")
        self.__account=50
        print(self.__account)
       
        self.__deposite=int(input("eneter new balance:"))
        self.final=int(self.__account)+int(self.__deposite)
    def read(self):
        print("account holder:")
        print("new account :", self.final)
data=full()

 

data.read()