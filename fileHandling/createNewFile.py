# 'x'-Creates- Will create a new file, returns an error, if the file exist.

f = open("demo.txt", 'x') # creates a new empty file
f.write("A new file.")
f.close()

# f = open("text.txt", 'x') # returns error
# f.close()

f = open("demo.txt", 'r')
print(f.read())


# 'a'-Append- Will create and append content into a file if the specified file doesn't exist.
# 'w'-Write- Wiil create and overwrite the content from a file if the specified file doesn't exist.
