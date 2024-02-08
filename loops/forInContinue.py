# continue: Skips the current iteration and proceeds to the next iteration of the loop.

print("\nOdd Numbers in between 0 and 20\n")

for i in range(100):
    if i%2 == 0:
        continue
    if i >= 20:
        break
    print(i)

print("\nend.")    
