#In python a moduleis a file containing python definitions and statements.
#The file name is the module name with the sufix .py appended

#Definitions from a module can be imported into other modules or into a main module

#this file operations.py just is a module. Lets create two function

def sum(num1,num2):
    print("Total Sum is: ", num1 + num2)
    

def sub(num1,num2):
    print("Total Subtraction is: ", num1 - num2)
    
#to test this module, in your terminal go to the dir 5_modules
#start the python interpreter: type: python
#import our module. type: import operations
#now our module can be used
#type: operations.sum(2,2)
#type: operations.sub(3,2)

#now we used the module and this module can be used at any time

#on the next examples, we will use it inside other files