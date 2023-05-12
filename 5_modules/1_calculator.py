#A module can be imported in other modules or scripts, using import statements at the beginning of file
from operations import sum, sub
#importing a module on a struct of dir lib/count
import lib.count # OR from lib import count
#if you wants import all function: from operations import *
#if you call this way: import operations you have that use this way: operations.sum()

#here we can use the module

sum(2,2)

sub(5,1)

#Here we can use the module of other directorie
fruits = ['apple', 'orange']
print(lib.count.arraylenght(fruits)) #OR count.arraylenght(fruits) if from lib import count


#to execute this on the terminal type: py .\5_modules\1_calculator.py