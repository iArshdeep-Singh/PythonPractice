iList = ["apple", "banana", "orange", "banana", "cherry", 1, 3, 5, 7, 11, 3.14, 2.0]

print(iList, "\n")

# Loop through the list items by using a 'for' loop

for i in iList:
    print(i)


# Loop through the index numbers
# Use the 'range()' and 'len()' fuctions to create a suitable iterable
print("\n", range(len(iList)))

for i in range(len(iList)):
    print(i)


# While Loop (Use 'len()' to determine the length)

print(iList, "\n")

i = 0

while i < len(iList):
    print(iList[i])
    i+=1


# Short hand 'for' loop that will print all items in a list.

print(iList, "\n")

[print(x) for x in iList]