print("\n1 for a Coffee\n2 for a Tea\n3 for a Juice")

choice = int(input("\nEnter A Number: ")) 

print("----------------------------------------------------------------------------------")

# coffee slection
if choice == 1: 
    print("Coffees: ")
    print("\t1 for Columbian Coffee\n\t2 for Java Coffee")
    coffeChoice = int(input("\n\tEnter A Number: "))
    print("----------------------------------------------------------------------------------")
    # columbian coffee slection
    if coffeChoice == 1:
        print("Columbian Coffee: ")
        print("\t\t1 for Small\n\t\t2 for Medium\n\t\t3 for Large\n")
        columbianCoffee = int(input("\t\tEnter A Number: "))
        print("----------------------------------------------------------------------------------")
        if columbianCoffee == 1:
            print("\t\tSmall Columbian Coffee")
        elif columbianCoffee == 2:
            print("\t\tMedium Columbian Coffee")
        elif columbianCoffee == 3:
            print("\t\tLarge Columbian Coffee")
        elif columbianCoffee > 3 or columbianCoffee == 0:
            print("\t\tInvalid Size Choice")
        elif columbianCoffee < 0:
            print("\t\tNegative Size Not Allowed") 
    # java coffee selection        
    elif coffeChoice == 2:
        print("Java Coffee: ")
        print("\t\t1 for Small\n\t\t2 for Medium\n\t\t3 for Large\n")
        javaCoffee = int(input("\t\tEnter A Number: "))
        print("----------------------------------------------------------------------------------")
        if javaCoffee == 1:
            print("\t\tSmall Java Coffee")
        elif javaCoffee == 2:
            print("\t\tMedium Java Coffee")
        elif javaCoffee == 3:
            print("\t\tLarge Java Coffee")
        elif javaCoffee > 3 or javaCoffee == 0:
            print("\t\tInvalid Size Choice")
        elif javaCoffee < 0:
            print("\t\tNegative Size Not Allowed")
    # invalid choice of coffee
    elif coffeChoice > 2 or coffeChoice == 0:
        print("\t\tInvalid Drink Choice")
    # negative drink choice of coffee   
    elif coffeChoice < 0:
        print("\t\tNegative Drink Not Allowed")

# tea selection
if choice == 2:
    print("Teas: ")
    print("\t1 for Earl Grey Tea\n\t2 for Green Tea")
    teaChoice = int(input("\n\tEnter A Number: "))
    print("----------------------------------------------------------------------------------")
    # earl grey tea slection
    if teaChoice == 1:
        print("Earl Grey Tea: ")
        print("\t\t1 for Small\n\t\t2 for Medium\n\t\t3 for Large\n")
        earlGreyTea = int(input("\t\tEnter A Number: "))
        print("----------------------------------------------------------------------------------")
        if earlGreyTea == 1:
            print("\t\tSmall Earl Grey Tea")
        elif earlGreyTea == 2:
            print("\t\tMedium Earl Grey Tea")
        elif earlGreyTea == 3:
            print("\t\tLarge Earl Grey Tea")
        elif earlGreyTea > 3 or earlGreyTea == 0:
            print("\t\tInvalid Size Choice")
        elif earlGreyTea < 0:
            print("\t\tNegative Size Not Allowed") 
    # green tea selection       
    elif teaChoice == 2:
        print("Green Tea: ")
        print("\t\t1 for Small\n\t\t2 for Medium\n\t\t3 for Large\n")
        greenTea = int(input("\t\tEnter A Number: "))
        print("----------------------------------------------------------------------------------")
        if greenTea == 1:
            print("\t\tSmall Green Tea")
        elif greenTea == 2:
            print("\t\tMedium Green Tea")
        elif greenTea == 3:
            print("\t\tLarge Green Tea")
        elif greenTea > 3 or greenTea == 0:
            print("\t\tInvalid Size Choice")
        elif greenTea < 0:
            print("\t\tNegative Size Not Allowed")
    # invalid choice  of tea
    elif teaChoice > 2 or teaChoice == 0:
        print("\t\tInvalid Drink Choice")
    # negative drink choice of tea   
    elif teaChoice < 0:
        print("\t\tNegative Drink Not Allowed")

# juice selection
if choice == 3:
    print("Juices: ")
    print("\t1 for Apple Juice\n\t2 for Orange Juice")
    juiceChoice = int(input("\n\tEnter A Number: "))
    print("----------------------------------------------------------------------------------")
    # apple juice selection
    if juiceChoice == 1:
        print("Apple Juice: ")
        print("\t\t1 for Small\n\t\t2 for Medium\n\t\t3 for Large\n")
        appleJuice = int(input("\t\tEnter A Number: "))
        print("----------------------------------------------------------------------------------")
        if appleJuice == 1:
            print("\t\tSmall Apple Juice")
        elif appleJuice == 2:
            print("\t\tMedium Apple Juice")
        elif appleJuice == 3:
            print("\t\tLarge Apple Juice")
        elif appleJuice > 3 or appleJuice == 0:
            print("\t\tInvalid Size Choice")
        elif appleJuice < 0:
            print("\t\tNegative Size Not Allowed") 
    # orange juice selection        
    elif juiceChoice == 2:
        print("Orange Juice: ")
        print("\t\t1 for Small\n\t\t2 for Medium\n\t\t3 for Large\n")
        orangeJuice = int(input("\t\tEnter A Number: "))
        print("----------------------------------------------------------------------------------")
        if orangeJuice == 1:
            print("\t\tSmall Orange Juice")
        elif orangeJuice == 2:
            print("\t\tMedium Orange Juice")
        elif orangeJuice == 3:
            print("\t\tLarge Orange Juice")
        elif orangeJuice > 3 or orangeJuice == 0:
            print("\t\tInvalid Size Choice")
        elif orangeJuice < 0:
            print("\t\tNegative Size Not Allowed")
    # invalid choice of juice        
    elif juiceChoice > 2 or juiceChoice == 0:
        print("\t\tInvalid Drink Choice")
    # negative drink choice of juice    
    elif juiceChoice < 0:
        print("\t\tNegative Drink Not Allowed")

# invalid choice
elif choice > 3 or choice == 0:
    print("----------------------------------------------------------------------------------")
    print("Invalid Drink Choice")

# negative choice
elif choice < 0:
    print("----------------------------------------------------------------------------------")
    print("Negative Drink Not Allowed")


# Name & Roll Number
print("\n\nName: ")
print("Roll Number: \n")