#“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. 
# However, there is a convention that is followed by most Python code: a name prefixed with an underscore

class MyClass:
    def __init__(self):
        self._private_var = 42

    def _private_method(self):
        return "This is a private method."

    def public_method(self):
        print("Accessing private variables/methods from public method:")
        print(f"Private variable: {self._private_var}")
        print(f"Private method: {self._private_method()}")


# Creating an instance of the class
obj = MyClass()

# Accessing private variable (not recommended)
print(obj._private_var)  # Output: 42

# Accessing private method (not recommended)
print(obj._private_method())  # Output: This is a private method.

# Accessing private variables/methods from a public method
obj.public_method()