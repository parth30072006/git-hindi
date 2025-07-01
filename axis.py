import numpy as np

n = np.array([[1,2,10,4],[5,6,7,8],[900,100,110,120]])

print("Original array:\n", n)
print("minimum value along axis 0:", n.min(axis=0))
print("minimum value along axis 1:", n.min(axis=1))