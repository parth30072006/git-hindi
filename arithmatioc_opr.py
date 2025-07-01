import numpy as np

n1 = np.array([15,20,25])
n2 = np.array([5,10,15])

print("Array n1:", n1)
print("Array n2:", n2)

ressr = np.sum([n1,n2])
print("Sum of n1 and n2:\n", ressr)

ressr = np.sum([n1,n2], axis=0) # axix=0 sums along the rows
print("Sum of n1 and n2:\n", ressr)