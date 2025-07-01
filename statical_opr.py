import numpy as np

n1 = np.array([5,10,15,20])
n2 = np.array([25,30,35,40])

print("Array n1:", n1)
print("Array n2:", n2)

resmean1 = np.mean(n1)
resmean2 = np.mean(n2)

print("mean of n1:",  resmean1)
print("mean of n2:", resmean2)

print("\n")

resmedian1 = np.median(n1)
resmedian2 = np.median(n2)

print("meandian of n1:",  resmedian1)
print("meandian of n2:",  resmedian2)

print("\n")

std1 = np.std(n1)
std2 = np.std(n2)

print("std of n1:",  std1)
print("std of n2:",  std2)