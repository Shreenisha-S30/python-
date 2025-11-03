#spliting method
import numpy as np

a = np.array([1,2,3,4,5,6,7])
result = np.array_split(a,3)
print(result)

b = np.array([[1,2,3,4],[5,6,7,8]])
h = np.hsplit(b,2)
print(h)


b = np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
v = np.vsplit(b,2)
print(v)
