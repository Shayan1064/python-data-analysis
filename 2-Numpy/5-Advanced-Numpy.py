import numpy as np

arr=np.array([1,2,4,5,6,7])
new=np.insert(arr,2,3)
print(new)

arr_2d=np.array([[1,2],[3,4]])
new_arr=np.insert(arr_2d,0,[5,6],axis=0)
print(new_arr)

arr_2d=np.array([[1,2],[3,4]])
new_arr=np.insert(arr_2d,0,[5,6],axis=1)
print(new_arr)

# Merge Array

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.concatenate((arr1,arr2)))

# Deleting elemnet

arr3=np.delete(arr,0)
print(arr3)

#   Stacking
print(np.hstack((arr1,arr2)))

print(np.vstack((arr1,arr2)))