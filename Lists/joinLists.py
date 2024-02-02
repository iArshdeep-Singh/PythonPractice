# There are several ways to join, or concatenate two or more lists in Python

iList = ["apple", "banana", "orange", "banana", "cherry"]
iListNumeric = [7, 11, 1, 3, 5]

print(iList, "\n")


# One of the easiest ways are by using '+' operator

newList = iList + iListNumeric

print(newList, '\n')


# Another way to join two lists is by appending all the items from iList into iListNumeric, one by one

for i in iListNumeric:
    iList.append(i)

print(iList, '\n')


# Or use the 'extend()' method to add iListNumeric at the end of iList

iList.extend(iListNumeric)

print(iList, '\n')