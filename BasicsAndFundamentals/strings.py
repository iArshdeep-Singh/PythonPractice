# Strings in Python are surrounded by eiter single qoutation marks, or double qoutation marks.
x = "Hello"
y = 'hello'

print(x)
print(y, '\n')


# Multiple Stings: A multiple string can be assigned to a variable by using three double/single qoutes.
# NOTE: In the result, the line breaks are inserted at the same position as in the code.
a = '''Lorem ipsum dolor sit amet,
weruqwio weiruqwio sdb aoens apaw ms weoieur wbo cbam cxo wenwe we,
weiowe wenweweopwe, weiwe w weow, 
weueu!@$#$@#%@#%$#$@##!@#!@#!@!#!@#!@#@@#'''

b = """Lorem ipsum dolor sit amet,
weruqwio weiruqwio sdb aoens apaw ms weoieur wbo cbam cxo wenwe we,
weiowe wenweweopwe, weiwe w weow, 
weueu!@$#$@#%@#%$#$@##!@#!@#!@!#!@#!@#@@#"""

print(a)
print(b, '\n')


# Strings Are Arrayas: Like many other popular programming languages, strings in Pyhton
# are arrays of bytes representing unicode characters.

# However, Python doesn't have a chracter data type, 
# a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

x = "Hello, world!"

print(x[1], '\n')


# Looping Through A String: Since strings are arrays, we can loop through the characters
# in a string, with a 'for loop'

for x in "banana":
    print(x)

print('\n')


# len(): Returns the length of a string
x = "Hello, Mars!"

print(len(x), '\n')


# Check String: To check, if a certain phrase or character is present in a string, we can 
# use the keyword 'in'
txt = "The best things in life are free!"

print("free" in txt)


# Check if NOT: Use the keyword 'not in'
txt = "The end of one thing is the start of something new"

print("Earth" not in txt)
print("one" not in txt, '\n')


