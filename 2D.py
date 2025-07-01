import numpy as np

n = np.array([[1,2,3],[4,5,6]])
print(n[0,0])  # Accessing the first element
print(n[0,1])  # Accessing the second element in the first row
print(n[1,0])  # Accessing the first element in the second row
print(n[0:2, 0:2])  # Slicing the first two