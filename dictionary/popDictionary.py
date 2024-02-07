# pop(keys, [ , default]): Removes and returns the values for the specified key.
# If the key isn't found, it returns the default value(if provided) or raise a key error.

iDictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

i = iDictionary.pop("brand")

print(i)
print(iDictionary)

