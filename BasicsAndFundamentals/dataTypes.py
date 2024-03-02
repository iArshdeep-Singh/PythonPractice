# In programming data type is an important concept.
# Variables can store data of different types, and different types can do different things
# Python has the following data types built-in by default, in these catagories:

# Text Type:        str
# Numeric Types:    int, float, complex
# Sequence Types:   list, tuple, range
# Mapping Type:     dict
# Set Types:        set, frozenset
# Boolean Type:     bool
# Binary Types:     bytes, bytearray, memoryview
# None Type:        None


# str
a = "Hello, World!" 
print(a)

# number
b = 20
print(b)

# float
c = 20.5
print(c)

# list
d = ["apple", "banana", "orange"]
print(d)

# tuple
e = ("apple", "banana", "orange")
print(e)

# range
f = range(6)
print(f)

# dict
g = {"name": "John", "age": 36}
print(g)

# set
h = {"apple", "banana", "cherry"}
print(h)

# frozenset
i = frozenset({"apple", "banana", "cherry"})

# bool
j = True
print(j)

# bytes
k = b"Hello"
print(k)

# bytearray
l = bytearray(5)
print(l)

# memoryview
m = memoryview(bytes(5))
print(m)

# none
n = None
print(n)


print('\n')


# SETTING THE SPECIFIC DATA TYPE

ax = str("Hello, world")
print(ax)

bx = int(20)
print(bx)

cx = float(20.5)
print(cx)

dx = complex(1j)
print(dx)

ex = list(("apple", "banana", "orange"))
print(ex)

fx = tuple(("apple", "banan", "cherry"))
print(fx)

gx = range(6)
print(gx)

hx = dict(name = "Python", age = 36)
print(hx)

ix = set(("apple", "banana", "cherry"))
print(ix)

jx = frozenset(("apple", "banana", "orange"))
print(jx)

kx = bool(5)
print(kx)

lx = bytes(5)
print(lx)

mx = bytearray(5)
print(mx)

nx = memoryview(bytes(5))
print(nx)   