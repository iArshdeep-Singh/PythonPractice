# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable created the moment you first assign a value to it.
# Variable don't need to be declared with any particular type, and can even change type after they have been set.

x = 5
y = "John"

print(x)
print(y)

# To specify the data type of a variable, this can be done with casting

x = str(3)
y = int(3)
z = float(3)

print(type(x))
print(type(y))
print(type(z))

# String variables can be declared either by using single or double qoutes

x = "John"
x = 'John'

print(x)

# Variable names are case-sensitive

x = 4
X = "Python"

print(x)
print(X)