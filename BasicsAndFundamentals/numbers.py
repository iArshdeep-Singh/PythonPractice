# There are three numeric types in Python:
# int, float, complex


# INTEGER: Int, or integer, is a whole number, positive or negative, without decimals,
# of unlimited length
x = 1
y = 12345678900987654321
z = -102938

print(type(x))
print(type(y))
print(type(z))


# FLOATING POINT NUMBER: Float, or "floating point number" is a number, positive or 
# negative, containing one or more decimals
x = 1.10
y = 1.0
z = -25.75

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power fo 10
x = 35e3
y = 12E4
z = -67.78e100

print(type(x))
print(type(y))
print(type(z))


# COMPLEX: Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


# TYPE CONVERSION
# Values of variable can convert from one type to another type with the int(), float(), and complex() methods.
x = 1
y = 2.5
z = 5j

# convert from int to float
a = float(x)

# convert from float to int
b = int(y)

# convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

x = float()
print(x)

y = complex()
print(y)

print("Complex numbers can't be converted into another number type.")


# RANDOM NUMBER
# Python doesn't have a "random()" function to make a random, 
# but Python has a built-in module called "random" that can be used to make random numbers.

# import the 'random' module
import random

print(random.randrange(1, 10)) # random number between 1 and 9