import numpy as np

# Sample array
arr = np.array([5, 10, 15, 20, 25, 30])

# 1. Basic filtering (most used)
greater_than_15 = arr[arr > 15]
print(greater_than_15)

# 2. Multiple conditions (AND)
between_10_30 = arr[(arr > 10) & (arr < 30)]
print(between_10_30)

#4 Or Gate
or_gate=arr[(arr > 10) | (arr < 40)]
print(or_gate)


# 3. Even numbers
even_numbers = arr[arr % 2 == 0]
print(even_numbers)