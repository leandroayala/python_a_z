#inheritance is for to use methods and attributer from the inheritader class
#Derived classes may override methods of their base classes.

#lets make a exeample many times used in other examples (rss)

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")


#here on the classe Dog we inherit from Animal
class Dog(Animal): #this is a sintax: Dog(Animal) : Dog inheting from Anmial
    def __init__(self, name):
        super().__init__(name) #here we inherit from call __init__ from Animal

    #here Dog 
    def sound(self):
        super().sound()
        


# Creating an instance of the Dog class
my_dog = Dog("Buddy")
#using a method inherited from Animal
my_dog.sound()