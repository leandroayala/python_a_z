# lists also known as arrays
# python lists can contain multiples types of elements
# For to execute this strings.py, on the terminal type: py .\types\lists.py

list = [1,2,3,4]
print(list)

list2 = [1,2,'a','b']
print(list2)

#like strings, lists can indexed and sliced
print(list[2])
print(list[0:4])
print(list[:])

#concatenating a list
list1 = [1,2]
list2 = [3,4]

list = list1 + list2
print(list)

#List are immutable
#we can change someone item from a list
list = [1,2,3]
list[2] = 9
print(list)

#We can add new items to the list
list = [1,2]
list.append(3)
print(list)

#function len() to lists
len = len(list)
print(len)
