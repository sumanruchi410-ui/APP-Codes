# NumPy array operations

import numpy as np

# Create NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Create 0-D array
arr = np.array(42)
print(arr)

# Access element from 2-D array
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])
print("2nd element on 1st row:", arr[0, 1])

# Find sum of array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Sum of array:", np.sum(arr))

# Array slicing
print("Sliced array:", arr[2:7])

# Generate random numbers
random_arr = np.random.randint(1, 100, 5)
print("Random numbers:", random_arr)