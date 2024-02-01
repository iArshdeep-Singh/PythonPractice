# Operators are used to perform operations on variables and values.

# ARITHMETIC OPERATORS
x = 12
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)  # Modulus
print(x ** y) # Exponentiation 
print(x // y, '\n') # Floor Division


# ASSIGNMENT OPERATORS
x = 3
print(x)

x += 3
print(x)

x -= 3
print(x)

x *= 3
print(x)

x /= 3
print(x)

x %= 3
print(x)

x **= 3
print(x)

x //= 3
print(x, '\n')


# COMPARISON OPERATORS
x = 3
y = 7

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y, '\n')


# LOGICAL OPERATORS: Used to combine conditional statements
x = 3
y = 5
z = 7

print(x < y and y > x and z > y)
print(x > y or y < x or z > y)
print(not(x < y and y > x and z > y), '\n')  # Reverse the result, returns False if the result is True


# IDENTITY OPERATORS: Used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory loction.
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# 'is' operator
print(x is y)
print(x is z)
print(z is y)
print(z is x, '\n')

# 'is not' operator
print(x is not y)
print(x is not z)
print(z is not y)
print(z is not x, '\n')


# MEMBERSHIP OPERATORS: Used to test if a sequence is presented in an object.
x = ["Earth", "Mars", "Pluto"]

# 'in' operator
print("Earth" in x)

# 'not in' operator
print("Earth" not in x)