iList = ["apple", "banana", "orange", "banana", "cherry", 1, 3, 5, 7, 11, 3.14, 2.0]

print(iList, "\n")


# The 'remove()' method removes the specified item
# If there are more than one item with the specified value, the 'remove()' method removes
# the first occurance

iList.remove("banana")

print(iList, "\n")


# Remove Specified Index: The 'pop()' method removes the specified index

iList.pop(1)

print(iList, "\n")


# If you don't specify the index, the 'pop()' method removes the last item.

iList.pop()

print(iList, "\n")


# The 'del' keyword also removes the specified index

del iList[-2]

print(iList, "\n")


# The 'clear()' method empties the list.
# The list stiil remains, but it has no content

iList.clear()
print(iList, "\n")


# The 'del' keyword can also delete the list completely

del iList

print(iList, "\n")