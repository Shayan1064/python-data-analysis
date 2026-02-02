# ---------- Tuple Properties ----------

tup = (10, 20, 30, 40, 20)

print("Tuple:", tup)

# 1. Length
print("Length:", len(tup))

# 2. Indexing
print("First element:", tup[0])

# 3. Slicing
print("Slice (1:4):", tup[1:4])

# 4. Reverse tuple
print("Reversed tuple:", tup[::-1])

# 5. Count method
print("Count of 20:", tup.count(20))

# 6. Index method
print("Index of 30:", tup.index(30))

# 7. Different data types
mixed_tup = (1, "Python", 3.14, True)
print("Mixed tuple:", mixed_tup)

# Tuples are immutable
# tup[0] = 99   # ❌ This will cause an error


print("\n---------- Palindrome Logic (Tuple) ----------")

pal_tup = (1, 0, 1)

rev_tup = pal_tup[::-1]

if pal_tup == rev_tup:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
