# __str__(): The '__str__()' function controls what should be returned when the class object
# is represented as a string.

class ClassX:
    def __init__(iSelf, x, y):
        iSelf.x = x
        iSelf.y = y

    def iCalc(iSelf):
        i = iSelf.x + iSelf.y
        print("x + y = ", i)        
        return i
    
    def __str__(iSelf):
        return f"{iSelf.x} and {iSelf.y}"
    

i = ClassX(1300, 700)

i.x = 1000

i.iCalc()
print(i.iCalc())
print(i)
