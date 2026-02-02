import numpy as np

#   How to Find missing value
arr=np.array([1,np.nan,2,3,4,5,np.nan])
print(arr)
print(np.isnan(arr))

# How to fill Missing Value
new=np.nan_to_num(arr,nan=9)
print(new)