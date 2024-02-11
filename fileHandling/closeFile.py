# It's a good practice to always close the file, after everything done with it.

f = open("text.txt", "r")

print(f.read())

f.close()