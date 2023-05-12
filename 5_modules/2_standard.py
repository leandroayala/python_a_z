#standard modules are a library os modules that comes in python
#a very used standard module is sys
import sys,operations


#The variable sys.path is a list of strings that determines the interpreter’s search path for modules.
print(sys.path)

#The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:
print(dir(operations))
