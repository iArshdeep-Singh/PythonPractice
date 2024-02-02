# List comprehension offers a shorter syntax when you want to create a new list based on the
# values of an existing list.

iList = ["apple", "banana", "orange", "banana", "cherry"]

print(iList, "\n")


# Without list comprehension you will have to write a 'for' statement with a conditional
# test inside

newList = []

for i in iList:
    if "a" in i:
        newList.append(i)

print(newList, "\n")


# With list comprehensive - all do that with only one line of code

otherNewList = [i for i in iList if "a" in i]

print(otherNewList, '\n')


# Condition: is like a filter that only accept the item that valuate to 'True'

anotherNewList = [i for i in iList if i != "apple"]

print(anotherNewList, '\n')


# The condition is optional and can be omitted
# With no 'if' statement

oneMoreNewList = [i for i in iList]

print(oneMoreNewList, '\n')


# Use 'range()' to create an iterable.

newListAgain = [i for i in range(10) if i < 5]

print(newListAgain, '\n')


# Experiments:

newList = [x.upper() for x in iList]

print(newList, '\n')


newList = ['hello' for x in iList]

print(newList, '\n')


newList = [x if x != "banana" else "orange" for x in iList]

print(newList, '\n')