#The list has some methods. Lets see!

#Lets create a list
#            0         1        2       3         4        5  
fruits = ['orange', 'apple', 'pear', 'orange', 'banana','lemon']
print(fruits)

#for add a item to the end of the list
fruits.append('pinnaple')
print(fruits)

#for add all elements of an iterable(list, tuple, string) to the end of the list
brazil_fruits = ['acerola', 'seriguela']
fruits.extend(brazil_fruits)
print(fruits)

#for add a item at given posicion. the first argument is the index of the element before which to insert
#in this exemple, the item will be inserted before apple element
fruits.insert(1,'strawberry')
print(fruits)

#for delete the first element which equal value, use this function
#in this list we have two orange elements: position 0 and 3
#so the method will be remove the first (position 0) 
fruits.remove('orange') 
print(fruits)

#For remove the item at give position in the list, and return
#if no index is specifield, will be the last element of the list and returned
element = fruits.pop(2)
print(fruits)
print("Element removed:",element)

fruits.pop()
print(fruits)

#for count the number of times a element exists on the list
banana_count = fruits.count('banana')
print('bananas',banana_count)

#for sort the itens in asceding or descending order
fruits.sort(reverse=True)
print(fruits)

#ther sort has the two optinal params. key, reverse
#here we will use the reverse=True for descending sort
fruits.sort(reverse=True)
print(fruits)

#For copy a list
fruits2 = fruits.copy()
print('fruits 2: ',fruits2)

#for remove all itens of the list
fruits.clear()
print(fruits)

#to execute this on the terminal type: py .\4_data_structures\1_list_methods.py