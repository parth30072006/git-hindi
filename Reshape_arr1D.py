import numpy as np

n = np.array([1, 2, 3, 4, 5,6,7,8,9,10])
print(n)

resize = n.reshape(2,5)
print("Reshaped array to 2 rows and 5 columns:", resize)
