#List comprehensions provide a concise way to create lists

#a way more common of create list
numbers = [] #declaring a number list

#Lets fill the list
for i in range(10):
    numbers.append(i)

print(numbers)

#A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

#Other form to create a list
numbers = [ x for x in range(10)]

print(numbers) 

#we can to use if condiction too
numbers = [ x for x in range(10) if x < 5]

print(numbers)

#to execute this on the terminal type: py .\4_data_structures\4_list_comprehenson.py