iList = ["apple", "banana", "cherry", 1, 3, 5, 7, 11, 3.14, 2.0]

print(iList, "\n")

iList[2] = "cheeku"
iList[3] = "one"

print(iList, "\n")


# Change a Range of item Values

iList[1:3] = ["amrud", "kela"]

print(iList, "\n")


# Change the second value by replacing it with two new values

iList[1:2] = ["guava", "pineapple"]

print(iList, "\n")


# Change the second and third value by replacing it with one value

iList[1:3] = ["orange"]

print(iList, "\n")


# Insert Items: The 'insert(index, item)' method inserts an item at the specified index.

iList.insert(0, "mint")

print(iList, "\n")