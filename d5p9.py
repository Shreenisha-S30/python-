import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

result = np.concatenate((a,b))
print("Concatenate:",result)

import numpy as np
x= np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])

result2 = np.concatenate((x,y), axis=0) #1 is for row and 0 is for coloumn
print("\nconcatenate:\n",result2)