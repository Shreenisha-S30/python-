import numpy as np
a = np.array([10,20,30,40,50])

result = np.where(a == 30)
print("Index where value is 30:",result)

a = np.array([10,15,20,25,30])
even_indexes = np.where(a % 2 == 0)
print("Even numbers:",a[even_indexes])

arr =np.array([10,20,30,40,50])
pos = np.searchsorted(arr,35) #first it will add then sort then finds the position
print("Inserted 35 at position: ",pos)

#ascending order
a = np.array([5,2,9,1,7])
print("Original array: ",a)

sorted_array = np.sort(a)
print("Sorted array: ", sorted_array)

#reverse
a = np.array([5,2,9,1,7])
print("Original array: ",a)

sorted_array = np.sort(a)
print("Sorted array: ", sorted_array)

reverse_array = sorted_array[::-1]
print("reversed arrary: ",reverse_array)

reverse_array = np.flip(a)
print("reversed arrary: ",reverse_array)