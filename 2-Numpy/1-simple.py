import numpy as np

# For single array
simple=np.array([1,2,3,4,5,6,7,8,9])
print(simple)


# For double array
double=np.array([[1,2,3],
                [34,5,6],
                [7,8,9]])
print(double)

# Reshaping Array
numbers=np.arange(0,16).reshape(4,4)
print(numbers)


# Zero Array
zeros=np.zeros((4,4))
print(zeros)


# One Array
ones=np.ones((4,4))
print(ones)


# Random Array
rand_num = np.random.randint(0, 10)
print(rand_num)

