#a way that we used to outptu in the previous examples was print()
#this function doesn't allow print formating
print("Print one")
print("Print two")
#Print to have some keywords arguments like sep=
print("one", "two","three", sep=" , ",)

#a way to formating output is using formatted string literals
#put a F/f before a string
#this will allow:
print(f'the year is is {2023}')

#if you need convert variables to print, on a debug for example
#using + to concatenate them
#tou can use str() or repr()
print('number '+ str(1) +   ' , ' + 'number '+ str(2) )

#repr() will genarate a string representation wich can be read by the interpreter
name = 'Ayala'
print('The variable name is ' + repr(name) )

#other way is using string.format() function
print("My name is {} {}".format('leandro','ayala'))

#Using keywords arguments
print('My Name is {firstName} {lastName}'.format(firstName='Leandro' , lastName='Ayala'))

#using keyword arguments and positional arguments
print('My name is {0} {1}. I\'m from {country}'.format('leandro','ayala', country='Brazil'))

