#ploting graphs
import matplotlib.pyplot as plt  
import numpy as np 
#plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,3,1)  #horizontal
plt.plot(x,y)
#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,2) #horizontal
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,2,7,6])

plt.subplot(2,3,3)
plt.plot(x,y)

x = np.array([3,4,5,6])
y = np.array([0,7,2,3])

plt.subplot(2,3,4)
plt.plot(x,y)

x = np.array([10,12,30,20])
y = np.array([0,7,2,3])

plt.subplot(2,3,5)
plt.plot(x,y)

x = np.array([3,4,5,6])
y = np.array([7,3,6,9])

plt.subplot(2,3,6)
plt.plot(x,y)

plt.show()