# There are ways to make a copy, one way is to use the buit-in List method 'copy()'

iList = ["apple", "banana", "orange", "banana", "cherry"]

print(iList, "\n")


# 'copy()' Method

newList = iList.copy()

print(newList, "\n")


# Another way to make a copy is to ue the built-in method 'list()'

otherNewList = list(iList)

print(otherNewList, "\n")

