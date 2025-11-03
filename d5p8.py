import numpy as np
a=np.array([10,20,30])
for x in a:
    print(x)
    
import numpy as np
a=np.array([[10,20,30],[40,50,60]])
print("\n2D Array Iteration:")
for row in a:
    print("Row:",row)
    for x in row:
        print(x)
        
import numpy as np
a=np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
print("\n3D Array Iteration:")
for block in a:
    print("Block:",block)
    for row in block:
        for x in row:
            print(x)