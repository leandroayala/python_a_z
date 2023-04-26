#Nested list are list that contain a sublist. Like a Matriz

#A nested list
nested = [1,['a','b','c'],2,['d','e','f']]
print(nested)
print(nested[1][0]) #print letter 'a'
print(nested[0]) #print 1

#We can use list comprehension to transpose line x columns
matriz= [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

new_matriz = [ [ row[i] for row in matriz] for i in range(4)]

print(new_matriz)

#its a same that

new_matriz = []

for i in range(4):
    transp_row =[]
    for row in matriz:
        transp_row.append(row[i])
    new_matriz.append(transp_row)

print(new_matriz)


#to execute this on the terminal type: py .\4_data_structures\5_nested_list_comprehenson.py