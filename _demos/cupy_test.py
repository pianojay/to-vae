import cupy as cp
import numpy as np

l = cp.array([4, 3, 21, 2])
l = cp.sort(l)

print(l)
print(type(l))
