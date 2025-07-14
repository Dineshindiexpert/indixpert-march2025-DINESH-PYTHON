class full:
    def __init__(self):
        self.__id=100
        self._name="dinesh"
        self.age=18
    def read(self):
        print("id purani:", self.__id)
data=full()
data.__id=101
data._name="ajay"
data.age=20
print(data.__id)
print(data._name)
print(data.age)

data.read()