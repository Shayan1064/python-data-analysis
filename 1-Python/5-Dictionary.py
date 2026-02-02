# ---------- Dictionary Properties & Methods ----------

myDict = {
    "name": "Shayan",
    "age": 21,
    "field": "Computer Science"
}

print("Original Dictionary:")
print(myDict)

# 1. keys() → returns all keys
print("\nKeys:")
print(myDict.keys())

# 2. values() → returns all values
print("\nValues:")
print(myDict.values())

# 3. items() → returns (key, value) pairs as tuples
print("\nItems:")
print(myDict.items())

# 4. get() → returns value of the given key
print("\nGet value using key:")
print(myDict.get("name"))      # existing key
print(myDict.get("city"))      # non-existing key (returns None)

# 5. update() → updates dictionary
newDict = {
    "age": 22,
    "city": "Peshawar"
}

myDict.update(newDict)

print("\nDictionary after update:")
print(myDict)





while True:
    key=input("Enter Key [OR] Exit to Leave: ")
    if key.lower()=='exit':
        break
    value=input("Enter Value: ")
    
    myDict[key]=value
    print(myDict)
    
print(myDict)