# elif

x = int(input("Enter your age: "))

if x >= 18:
    print("\nYou are an adult.")
elif x <= 13 and x < 18:
    print("\nYou are a teenager.")
else:
    print("\nYou are a child.")

print("\nCode is terminated.")    
