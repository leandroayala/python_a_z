#Sets are a other type of data structure
#A set is an undered collection with duplicate elements.
#Set objects also support mathematical operations like union, intersection, difference...

#to declare a set we use {} or set()
fruits = {'banana','orange','apple','orange'}

#To declare a empty set
setTest = set()

#If we print the set, the duplicate elements will be removed
print(fruits)

#to testing if a item exists
print('orange' in fruits)

#Set operations
a = set('abcdasb')
print('Set a: ',a)
b = set('dertgab')
print('Set b: ',b)

#letters in a but not in b
print(a-b)


#to execute this on the terminal type: py .\4_data_structures\7_sets.py