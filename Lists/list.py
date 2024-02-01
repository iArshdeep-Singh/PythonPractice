# Lists are used to store multiple items in a single variable
# Lists are created using square brackets

iList = ["apple", "banana", "cherry"]

print(iList, '\n')


# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
iList = ["apple", "apple", "banana", "cherry", "cherry"]

print(iList, '\n')


# List Length: To determine how many items a list has, use the 'len()' function.
iList = ["apple", "banana", "cherry"]

print(len(iList), '\n')


# Data Types: List items can be of any data type.
iList = ["apple", "banana", "cherry"]
iList_x = [1, 3, 5, 7, 11, 13]
iList_xl = [True, False, True, False]
iList_xxl = ["apple", 1, True, "banana", 3, False, "cherry", 5, True]

print(iList)
print(iList_x)
print(iList_xl)
print(iList_xxl, '\n')


# type()
iList = ["apple", "banana", "cherry"]

print(type(iList), '\n')


# The lis() Constructor
iList = list(("apple", "banana", "cherry")) # NOTE the double round-brackets

print(iList)