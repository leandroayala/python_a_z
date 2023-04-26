#Dictionaries in python are like associatives arrays in other languages
#dictionaries are indexed by keys

#declaring a dictionary
tels = {'ayala':3333222, 'john':999000}
print(tels)

#adding a new element
tels['mari'] = '88889999'
print(tels)

#removing a element
del tels['ayala']
print(tels)

#List to list elements
print(list(tels))

#To lopping dictionaries make:
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#to execute this on the terminal type: py .\4_data_structures\8_dictionaries.py