# To delete a file import the 'os' module

import os

# os.remove('demo.txt')


# check if doesn't exist

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("The file doesn't exist.")