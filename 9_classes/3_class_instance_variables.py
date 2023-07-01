#Generally speaking, instance variables are for data unique to each instance 
#and class variables are for attributes and methods shared by all instances of the class

class Car:
    #attributes
    kind = 'veicle'
    
    #method to excuted on each instance
    def __init__(self,name):
        self.name = name
        
        
#how we isntancing the class
#the classe have a __init__ method,so we need to put the parameters. in this case the "name" parameter
c = Car("ford 1235")

#now c is a instance of the Car classe we can use it
print("c instance: ",c.name)
print("c instance: ",c.kind)

#but notice that the kind atthibute is shared about all instance the class

d = Car("ferrari")
print("d instance: ",d.kind)
print("d instance: ",d.name)

#if we can to evite this, we have to use instance variables
#nothins else is method that will ti manipulate the varibles
class CarTwo:

    def __init__(self,name):
        self.name = name
        self.colors = [] #creates a list of the cars

    #here a method to manipulate the list of cars
    def addList(self,colors):
        self.colors.append(colors)

car = CarTwo("ferrari")
car.addList("black")
car.addList("red")
print(car.name)    
print(car.colors)

#if you to comment the method addList, you not will have to acess the "self.colors"



