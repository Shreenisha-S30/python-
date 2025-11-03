#write a python program to calculate the total marks of a student. the marks are stored in a list: [78,85,69,90,88]. 
# use for loop to add all marks and display the total
marks= [78,85,69,90,88]
total=0
for i in marks:
    total += i
print("total marks =",total)