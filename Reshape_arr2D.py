import numpy as np

n = np.array([[[[1,2,3],[4,5,6],[7,8,9]]]])
print("\n", n)

resize = n.reshape(-1)
print("Reshaped array to 1D:", resize)