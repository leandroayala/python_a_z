# to execute this if.py, on the terminal type: py .\2_control_flow\if.py

#before all we need know that identation is python's way of grouping statements

#the IF statement is very useful for decision make

color = 'blue'
anwser = ''

#If declaration: If (condicion):
if color == 'blue':
    #the tab here means that the next lines will be executed if condition was true  
    anwser = 'The color is blue'
#to a second statement, use else or elif
elif color == 'yellow':
    anwser = 'The color is yellow'
#the else statement will be executed if no condition above was true
else:
    anwser = 'any color found!'

#here you can continue your code
#here you are out ou if statement
print(anwser)
