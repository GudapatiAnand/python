# demo_list=[5,4,4,6,8,12,12,1,5]
# unique_list=list(set(demo_list))
# print(unique_list)

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.argsort()[ -5: ][::-1])