import matplotlib.pyplot as plt  
import numpy as np 
#plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)  #horizontal
plt.plot(x,y)
#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2) #horizontal
plt.plot(x,y)

plt.show()

import matplotlib.pyplot as plt  
import numpy as np 
#plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,1,1)  #vertical
plt.plot(x,y)
#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,1,2) #vertical
plt.plot(x,y)

plt.show()