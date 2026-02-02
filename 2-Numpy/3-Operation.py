import numpy as np

array=np.array([11,22,33,44,55,66,77,88])

print(np.sum(array))
print(np.mean(array))
print(np.median(array))
print(np.std(array))
print(np.var(array))
print(np.max(array))
print(np.min(array))



arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(np.mean(arr))        # Mean of ALL values
print(np.mean(arr, axis=0))  # Column-wise mean
print(np.mean(arr, axis=1))  # Row-wise mean
