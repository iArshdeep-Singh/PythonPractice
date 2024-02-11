# 'r'-Read- Default value. Opens a file for reading, returns error if file doesn't exist
# Use 'read()' method for reading content of the file.

f = open('text.txt', 'r')

# print(f.read())

# Read only parts of the file.

# print("\n", f.read(5))

# Read Lines

print(f.readline())
