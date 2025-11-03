import matplotlib.pyplot as plt  
import numpy as np 

xpoint = np.array([2,5,3,7])
ypoint = np.array([4,7,5,9])

plt.plot(ypoint, marker = 'o', linestyle = 'dotted')
plt.plot(xpoint, marker = 'o', linestyle = 'dashdot')
plt.show()