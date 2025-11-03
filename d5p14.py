#marks of 5 students in 3 subjects: [math,science,english]
#avg marks per subject
import numpy as np
marks = np.array([[85,78,92],[74,88,90],[90,94,89],[65,70,72],[80,85,85]])

avg_marks = np.mean(marks,axis=0)
print("Marks of math subject: ",avg_marks)

avg_marks1 = np.mean(marks,axis=1)
print("Marks of math subject: ",avg_marks1)

h_marks = np.max(marks , axis=0)
print("highest marks: ",h_marks)
l_marks = np.min(marks , axis=0)
print("highest marks: ",l_marks)
topper = np.argmax(avg_marks1) 
print("Top student (index): ",topper)
print("Topper's avg marks: ",avg_marks1[topper])