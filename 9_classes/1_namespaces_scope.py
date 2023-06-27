#Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, 
#allowing new instances of that type to be made. Each class
#instance can have attributes attached to it for maintaining its state. 
#Class instances can also have methods (defined by its class) for modifying its state.

#scope example

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


#nonlocal statement:  indicates that particular variables live in an enclosing scope and should be rebound there.
#global statement: can be used to indicate that particular variables live in the global scope and should be rebound there

#to execute: python