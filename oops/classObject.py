# Python is an object-oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A class is like an object constructor, or a 'blueprint' for creating objects.

# To create a class, use the 'class' keyword.

class MyClass:
    def __init__(self, arg):
        self.arg = arg

    def iFunction(i):
        print("arg: ", i.arg)

# __init__(): All classes have a function called '__int__()' which is always executed 
# when the class is being initiated. This method is automatically called when a new object
# is created. It initialize the object attributes.
# '__init__()' function is used to assign values to object properties, or properties that
# are neccessary to do when the object is being created.

i = MyClass(2000)

print(i.arg)
i.iFunction()

# self: The self parameter is a reference to the current instance of the class, and is used
# to access variables that belongs to the class.
# It doesn't have to be named 'self', call it whatever you like, but it has to be the first
# parameter of any function in the class.