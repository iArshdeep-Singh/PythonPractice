# A lambda function is a small anonymous function.
# A lambda can take any number of arguments, but can only have one expression
# Lamba functions are typically used for short, simple operations.
# Use 'lambda' keyword to define a lambda function.

add = lambda x, y: x  + y

print(add(1500, 500))

# Lambda fucntion allows you to use an anonymous function inside another function.

def iFunction(n):
    return lambda a: a * n

myDoubler = iFunction(2)

print(myDoubler(11))