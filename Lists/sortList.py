iList = ["apple", "banana", "orange", "banana", "cherry"]
iListNumeric = [7, 11, 1, 3, 5]

print(iList, "\n")


# 'sort()' method sorts the list alphanumerically, ascending, by default

iList.sort()
iListNumeric.sort()

print(iList, "\n")
print(iListNumeric, "\n")


# Sort Descending: To sort descending order, use the keyword argument 'reverse=True'

iList.sort(reverse=True)
iListNumeric.sort(reverse=True)

print(iList, "\n")
print(iListNumeric, "\n")


# The 'reverse()' method reverses the current sorting orderof the element

iListExp = ["apple", "kiwi", "banana", "mango", "orange", 3, 5, 1, 7]

print(iListExp, '\n')

iListExp.reverse()

print(iListExp, '\n')

