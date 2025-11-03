try:
    marks = int(input("Enter marks:"))
    if marks<0 or marks>100:
        raise ValueError("marks should be between 0 and 100")
    else:
        print("Marks accepted succesfully")
except ValueError as e:
    print("Error: ",e)
except Exception:
    print("Please enter numbers only!")
finally:
    print("program finished ")