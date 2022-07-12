li = [['a','b','c'], [1,2,3], ['x','y','z']]
print(sum(li, []))


li = {1:'one', 2:'two', 3:'three'}
print(sum(li, 0))


import numpy as np

data = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
    ]

print(np.sum(data))