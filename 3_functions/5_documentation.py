#For to document a function, to exists some conventions
#1. The first line should always be a short, concise summary of the object’s purpose
#2. If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.
#3. The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.

#let's make a exemple
def myName(name):
    """This function to return your name like: My Name is [name]
    
    The function to receive one string argument and print  a text in console
    It also returns the same sentence
    """
    sentence = "Your name is " + name
    print(sentence)
    return sentence

#If you want to see function documentation, do
print(myName.__doc__)
