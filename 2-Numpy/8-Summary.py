# ================================
# NUMPY COMPLETE BASIC SUMMARY
# ================================

# 1️⃣ Import NumPy
import numpy as np


# ================================
# 2️⃣ Creating NumPy Arrays
# ================================

# From list
arr1 = np.array([1, 2, 3, 4])
print("1D Array:", arr1)

# 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("2D Array:\n", arr2)


# ================================
# 3️⃣ Array Attributes
# ================================

print("Shape:", arr2.shape)     # rows, columns
print("Dimension:", arr2.ndim)  # number of dimensions
print("Data type:", arr2.dtype) # data type
print("Size:", arr2.size)       # total elements


# ================================
# 4️⃣ Different Ways to Declare Arrays
# ================================

zeros = np.zeros((2, 3))     # all zeros
ones = np.ones((2, 3))       # all ones
arange = np.arange(0, 10, 2) # range with step
linspace = np.linspace(1, 10, 5) # equal spacing
full = np.full((2, 2), 9)    # fixed value
eye = np.eye(3)              # identity matrix

print(zeros)
print(ones)
print(arange)
print(linspace)
print(full)
print(eye)


# ================================
# 5️⃣ Reshape
# ================================

nums = np.arange(0, 16)
reshaped = nums.reshape(4, 4)  # reshape to 4x4
print("Reshaped Array:\n", reshaped)


# ================================
# 6️⃣ Indexing & Slicing
# ================================

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])      # first element
print(arr[1:4])    # slicing
print(arr[-1])     # last element


# ================================
# 7️⃣ dtype and astype
# ================================

arr_float = np.array([1.2, 2.5, 3.8])
arr_int = arr_float.astype(int)  # convert float to int

print("Original dtype:", arr_float.dtype)
print("Converted dtype:", arr_int.dtype)


# ================================
# 8️⃣ Broadcasting
# ================================

# Broadcasting applies single value to entire array
price = np.array([100, 200, 300])
discount = 10  # percent

final_price = price - (price * discount / 100)
print("Final Prices:", final_price)


# ================================
# 9️⃣ Filtering (Very Important)
# ================================

data = np.array([5, 10, 15, 20, 25, 30])

# Basic filtering
print(data[data > 15])

# Multiple conditions
print(data[(data > 10) & (data < 30)])

# Even numbers
print(data[data % 2 == 0])

# where() function
print(np.where(data > 20, data, 0))


# ================================
# 🔟 Statistical Functions
# ================================

stats_arr = np.array([[1, 2, 3],
                      [4, 5, 6]])

print("Mean:", np.mean(stats_arr))
print("Row-wise Mean:", np.mean(stats_arr, axis=1))
print("Column-wise Mean:", np.mean(stats_arr, axis=0))

print("Median:", np.median(stats_arr))
print("Sum:", np.sum(stats_arr))
print("Min:", np.min(stats_arr))
print("Max:", np.max(stats_arr))
print("Std Dev:", np.std(stats_arr))


# ================================
# 1️⃣1️⃣ Random Numbers
# ================================

# Random float
print(np.random.rand(3))

# Random integer
print(np.random.randint(0, 10, size=5))


# ================================
# END OF NUMPY BASICS SUMMARY
# ================================
