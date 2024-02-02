iList = ["apple", "banana", "cherry", 1, 3, 5, 7, 11, 3.14, 2.0]

print(iList, "\n")


# To add an item to the end of the list, use the 'append()' method

iList.append("end")

print(iList, "\n")


# To inset a list item at a specified index, use the 'insert()' method

iList.insert(-1, "second last")

print(iList, "\n")


# Extend List: To append elements from another list to the current list, use the 'extend()' method

iList_x = ["one", "two", "three"]

iList.extend(iList_x)

print(iList, "\n")


# Add Any Iterable: The 'extend()' method can add any iterable object(tuple, sets, dictionaries etc.)

iTuple = ("kiwi", "orange")

iList.extend(iTuple)

print(iList, "\n")
