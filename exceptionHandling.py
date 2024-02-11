# Exception handling in Python involves anticipating and responding to erros that may
# occur during the execution of a program.

# It's about being ready for unexpected situations while a program runs.

def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Cannot divided by zero!")
    except TypeError:
        print("Invalid input!")
    else:
        print("Result: ", result)
    finally:
        print("Cleanup: Closing resources...\n")


divide(10, 2)        
divide(10, 0)        
divide("a", 2)        