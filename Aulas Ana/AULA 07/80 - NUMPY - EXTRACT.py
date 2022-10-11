import numpy as np


arr = np.arange(12).reshape((3, 4))

array = ([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

condition = np.mod(arr, 3)==0


array = ([[ True, False, False,  True],
       [False, False,  True, False],
       [False,  True, False, False]])

x = np.extract(condition, arr)
   


print(x)