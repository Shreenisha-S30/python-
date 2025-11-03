import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

result = np.stack((a,b), axis=0)
print("Stack along axis=0:\n",result)

result2 = np.stack((a,b), axis=1)
print("Stack along axis=1:\n",result2)

#join method
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

h = np.hstack((a,b))
v = np.vstack((a,b))

print("Horizontal:",h)
print("Vertical:",v)