# Variables that are created outside of a function are known as global variabes.
# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myFunc():
    print("Python is " + x)

myFunc()

# If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function. The global variable with the same name will remain
# as it was, global and with the original value.

x = "awesome"

def myFuncx():
    x = "fantastic"
    print("Python is " + x)

myFuncx()

print("Python is " + x)


# Normally, when a variable is created inside a function, that variables is local, and
# can only be used inside that function.
# To create a global variable inside a function, the 'global' keyword can be used.

def myFuncxl():
    global x 
    x = "fantastic"

myFuncxl()   

print("Python is " + x)
