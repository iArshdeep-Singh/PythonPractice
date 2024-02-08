# pass: 'if' statement cannot be empty, but if you for some reason have an 'if' statement
# with no content, put it in the 'pass' statement to avoid getting an error.
# It can be used as a placeholder for code that you plan to implement late.

x = int(input("Enter your age: "))

if x >= 18:
    # print("\nYou are an adult.")
    pass

print("\nCode is terminated.")    
