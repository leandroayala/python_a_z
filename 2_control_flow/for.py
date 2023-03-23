# to execute this if.py, on the terminal type: py .\2_control_flow\for.py

# the for statement iterates over iten of any sequence

#simple for irerating over a range of number
for i in range(5): #range() is a built-in function for iterating over numbers
    print("number -> " + str(i)) #str(i) to trnasform the number in string

#For iterating over a list
animals = ['cat', 'dog', 'elephant', ]

for animal in animals:
    print(animals)

#for to irate over a collection
users = {'leandro':'active', 'ayala':'inactive'}

#The return for the two properties of the collection: user, status
#users.items() for iterate the collection
for user, status in users.items():
    print(user + ' -> ' + status)
    

#it's possible to break a for statement using break command
#in this example the break command will break the for loop
for i in range(10):
    if i == 5:
        print('number 5')
        break
    else:
        print(i)

#the continue command is for continue with next iteration
#in this case, without "continue", the loop will print: found!!! 4 and number 4
#with continue command, the loop will print: found!!! 4 and number 5 
for num in range(10):
    if num == 4:
        print('found!!!',num)
        continue #comment and test
    print('number',num)    