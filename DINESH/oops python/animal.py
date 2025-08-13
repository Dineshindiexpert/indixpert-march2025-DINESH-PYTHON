from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    
    def sound(self):
        print("cat sound")

class Dog(Animal):
    
    def sound(self):
        print("dog sound")

class Sheep(Animal):
    def sound(self):
        print("sheep sound")

class Calling:
    
    def printsounds(self):
        cat = Cat()
        dog = Dog()
        sheep = Sheep()

        cat.sound()
        dog.sound()
        sheep.sound()

call = Calling()
call.printsounds()
