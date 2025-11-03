#write a python program to print the result above 60-first class, 45> <60 second class, 35-45 pass, below 35 fail
marks=int(input("Enter the marks:"))
if marks>=60:
    print("first class")
elif marks>=45 and marks<60 :
    print("second class")
elif marks>=35 and marks<45 :
    print("Pass")
else:
    print("Fail")
          