#all function can receive arguments
#the argumens are useful for getting values from out and to process
#like a function sum. its needs two number argumens

def sum(num1, num2):
    total = num1 + num2
    return total

#lets call the function and receive the result and print
result =sum(2,2)
print("Result Function SUM(): ", result)

#to execute on the terminal:  py .\3_functions\arguments.py

#If we call just sum() without params?
#we see on the terminal something like: TypeError: sum() missing 2 required positional arguments: 'num1' and 'num2'
#this is telling us that we must inform the two params
#remove the coment the two lines below and you will see the error message

#result = sum()
#print(result)

#in functions exists default arguments values
#lets create a function sum2
#comment the two line above to eliminate the error and execute the file again

def sum2(num1=0,num2=0):
    total=num1+num2
    return total

#the function can be called in several ways:

#without arguments, because the two arguments are default
result = sum2()
print("Result Function SUM2 without arguments",result)

#called with one argument
result = sum2(1)
print("Result Function SUM2 with one argument",result)

#called with one argument
result = sum2(1,5)
print("Result Function SUM2 with two argument",result)

#arguments Types

#Keyword argument
def function(color):
    print(color)

#we can calls the two forms
function('blue')
function(color = 'green')

#posicional arguments
def f(pos1, pos2):
    print(pos1)
    print(pos2)

#posicional arguments
#this form the posicion its important
def f(pos1, pos2,/): #here we use / for define that the arguments before / are positional arguments
    print(pos1)
    print(pos2)

#Only Keyword argument
def keyword_only(*, color): #define that the arguments after * are keyword arguments
    print(color)
    
#must be called this form
keyword_only(color="blue")
