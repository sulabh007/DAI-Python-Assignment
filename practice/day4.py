import numpy as np
from numpy import linalg as la

a= np.array([[5,3],[2,1]])
print(la.inv(a))
b= np.array([[1,1,0],[1,1,1],[0,2,1]])
print(la.inv(b))
