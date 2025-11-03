#write a python program to accept the student marks(out of 100)
#your program should handle invalid inputs using try and except
#requirements: ask the user to enter marks(for ex, enter marks:)
#if the input is not a number, show an error msg-- please enter numbers only
#if the marks are less than 0 or greater than 100, show--marks should be btw 0 and 100
#otherwise print--marks accepted successfully
#finally print--program finished 
try:
    marks = int(input("Enter marks:"))
    if marks>0 and marks<100:
        print("marks accepted successfully")
    else:
        print("Number should be between 0 to 100")
except ValueError:
    print(" please enter numbers only")
finally:
    print("program finished ")