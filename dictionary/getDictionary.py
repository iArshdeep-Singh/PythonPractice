# get(key, [ , default]): Returns the value for the specified key. 
# If the key isn't found, it returns the default value. (None by default)

iDictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(iDictionary.get("brand"))
print(iDictionary.get("apple"))
print(iDictionary.get("apple", "Not Found"))