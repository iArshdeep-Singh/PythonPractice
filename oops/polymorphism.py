# The 'polymorphism means' 'many forms' and in programming it refers to methods/functions
# /operators with the same name that can be executed on many objects or classes.

# Parent Class
class Vehicle():
    def __init__(self, brand, model):
        self.iBrand = brand
        self.iModel = model

    def move(self):
        print("move!\n")        


# Child Classes
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("sail!\n")

class Plane(Vehicle):
    def move(self):
        print("fly!\n")


# Objects

car = Car("Ford", "Mustang")        
boat = Boat("Ibiza", "Touring20")
plane = Plane("Boeing", "747")


for i in (car, boat, plane):
    print(i.iBrand)
    print(i.iModel)
    i.move()