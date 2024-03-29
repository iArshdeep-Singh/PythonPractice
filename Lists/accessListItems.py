# Lists are indexed and can be accessed by referring to the index number.

iList = ["apple", "banana", "cherry", 1, 3, 5, 7, 11, 3.14, 2.0]

print(iList, "\n")

# Positive Indexing
print("Positive Indexing: ", iList[0], "\n")


# Negative Indexing: Starts from the end.
# '-1' refers to the last item, '-2' refers to the second last item etc.
print("Negative Indexing: ", iList[-1], "\n")


# Range: A range of indexes by specifying where to start and where to end the range.
print("Positive Range: ", iList[2:5], "\n") # return the third, fourth and fifth item.


# Range of Negative Indexes:
print("Negative Range: ", iList[-4:-1], "\n")


# Check if Item Exists
print(2.0 in iList)