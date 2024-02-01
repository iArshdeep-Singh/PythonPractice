# Python allows you to assign values to multiple variables in one line.
x, y, z = "Snake", "Language", "Django"

print(x)
print(y)
print(z)

# One value to multiple variables
x = y = z = "Snake"

print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a lis, tuple etc. Python allows you-
# to extract the values into variables. This is called unpacking.

# EXAMPLE- 
# Unpack a list:

fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)
print(y)
print(z)