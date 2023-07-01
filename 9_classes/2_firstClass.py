class Myclass:
    """A simple example class""" 
    name = 'MyClass'
    
    def getName(self):
        return 'MyClass'

#name is a attribute on the class
#getName is a method on the class

#to get the attributes or methods of a class make:

print(Myclass.name)

print(Myclass.__doc__) #doc of the class - first line is the class

#for instanciate the class and to use their methods make:

m = Myclass() #this creat a new instance od the class. the m is a object
print(m)
print(m.getName())

#when a new instace of the classe is executed, it is a empty object
#many classes to create a initial state
#for this we use an __init__() method
class Car:
    def __init__(self):
        self.color = "blue"
        self.name = "ford"
    #here we definined a method to get te car color
    def getColor(self):
        return self.color
    #end here the name color
    def getName(self):
        return self.name
        

#when a new instance of the classe is executed, the __init__() method is executed
myCar = Car()
print(myCar.color)

#here is how we call a method of the class
print("the car color is: ", myCar.getColor())
print("the car color is: ", myCar.getName())

#we may to given arguments to the __init__() method
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = People("ayala", 30)
print(people.name)