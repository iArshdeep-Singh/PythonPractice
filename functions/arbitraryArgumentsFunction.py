# Functions can accept a variable number of arguments using '*args' and '**kwards'

# If number of arguments is unknown, add '*' before the parameter.

def iFunction(*x):
    print(x[2])
    return x[1]

y = iFunction("Earth", "Mars", "Jupiter", "Satrus")

print(y)


# arguments can also be set with KEY:VALUE syntax. This way the order of arguments doesn't matter.
# If the number of keyword arguments is unknown, add '**' before the parameter name.

def iFunctionX(**x):
    print(x["x"])
    return x["z"]

z = iFunctionX(x = "Naptune", y = "Earth", z = "Mars")

print(z)