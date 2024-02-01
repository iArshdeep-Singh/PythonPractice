# Booleans represent one of two values: True or False

print(10 < 2)
print(5 < 9)
print(10 == 9, '\n')


# Evaluate Values and Variables

# Will return 'True':
print(bool("apple"))
print(bool(124))
print(bool(["apple", "banana", "cherry"]), '\n')

# Will return 'False':
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}), '\n')


# Function can return a Boolean

def iFunction():
    return True

if iFunction():
    print("Yes!")
else:
    print("No!")
