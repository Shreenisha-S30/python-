#ploting graph with color,marker and linewidth
import matplotlib.pyplot as plt  
import numpy as np 

ypoint = np.array([3,8,1,10])

plt.plot(ypoint, c = '#9AEB89', marker ='o', linewidth = '3.5')
plt.show()