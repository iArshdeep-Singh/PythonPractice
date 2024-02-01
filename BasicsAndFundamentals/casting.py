# Casting refers to the process of converting a variable from one data type to another.

# There may be times, when you want to specify a type on to a variable. This can be done
# with casting. Python is an object-oriented language, and as such it uses classes to 
# define data types, including its primitive types.

# Casting in Python is therefore done using constructor functions.

# int(): Constructs an integer number from an integer literal, a float literal (by removing
# all decimals), or string literal (providing the string represents a whole number).
x = int(1)
y = int(1.25)
z = int("3")

print( x, "\n", y, "\n", z, "\n")

# float(): Constructs a float number from an integer literal, a float literal or 
# a string literal (providing the string represents a float or an integer).
x = float(2)
y = float(2.25)
z = float("4.75")

print( x, "\n", y, "\n", z, "\n")

# str(): Constructs a string from a wide variety of data types, including strings, integer
# literals and float literals.
x = str(3)
y = str(3.25)
z = str("78")

print( x, "\n", y, "\n", z, "\n")