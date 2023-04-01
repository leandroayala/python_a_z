## The lambda expressions can be used for  small anonymous function 
#lambda function is a expression

#this is a normal function
def add_one(x):
    return x + 1

#this is a lambda equivalent
lambda x: x + 1


#first example that returs a sum
#lambda expression can be assigned to a variable 
thelambda = lambda x,y: x + y
print(thelambda(1,2))
