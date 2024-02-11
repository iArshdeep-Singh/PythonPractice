# 'a'-Append- Will append to the end of the file. Create a file, if specified file doesn't exists.

f = open('text.txt', 'a')

f.write("Now the file has more content.")
f.close()

f = open('text.txt', 'r')

print(f.read())
f.close()

# 'w'-Write- Will overwrite any existing content.

f = open('text.txt', 'w')

f.write("Woops! I have deleted the content!")
f.close()

f = open('text.txt', 'r')

print(f.read())
f.close()


print("\n")


f = open("text.txt", 'r')

print(f.read())
f.close()