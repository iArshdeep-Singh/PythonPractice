# Inheritance allows to define a class that inherits all the methods and properties
# from another class.

# 'Parent class' is the class being inherited from, also called base class.
# 'Child class' is the class that inherits from another class, also called derived class.


# Parent Class
class Parent():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printName(selfi):
        print(f"{selfi.firstname} {selfi.lastname}")

iP = Parent("Mike", "Olsen")            

iP.printName()

# 'super()' function makes the child class inherit all the methods and properties from its parents.

# Child Class
class Child(Parent):
    def __init__(selfii, fname, lname, year):
    
        super().__init__(fname, lname) 

        selfii.graduationyear = year

    def welcome(selfiii):
        print(f"Welcome, {selfiii.firstname} {selfiii.lastname}, to the class of, {selfiii.graduationyear}.")



iC = Child("Arshdeep", "Singh", 2000)        

iC.welcome()
iC.printName()