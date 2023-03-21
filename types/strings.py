# stings in python can be enclosed in single quotes ('..') or double quotes ("..")
# For to execute this strings.py, on the terminal type: py .\types\strings.py

# single quotes
single = 'Hello world'
print(single)

#double quotes
double = "Hello world"
print(double)

# use \ to  scape the single quote
#you can use "" too
message = 'he doesn\'t'
print(message)

message = "he doesn't"
print(message)

#The other form
message = "'yes', he said"
print(message)

message = "\"yes\", he said"
print(message)

#strings on the terminal | print() function
# the \n means new line
print('hello \n world')

#in case you want to some..
print('C:\some\names')

#problem resolved
#use the r before the quote
print(r'C:\some\names')

#use """...""" or '''...''' to print multiple lines
#the \ 
print("""
helo
my friend! """)

#Strings concatenation
print('py' 'thon')
print(3 * 'bla')

#to break long lines use ()
longline = ('this is a long line that you ' 
'break in te code')
print(longline)

# strings can be indexed. the first character is 0
name = 'ayala'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[0:5])

#how you can know the length of a string
string_lenght = len('Leandro Ayala')
print(string_lenght)