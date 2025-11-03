#Create a Calculator with Multiple Operations and Exception Handling
print("----------Simple Calculator----------")
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        raise ZeroDivisionError("cannot divisible by zero")
    return x/y
        
def calculator():
    print("\n1. Addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. Division\n")
        
    try:
        choice = input("Enter the number for 1 to 4: ")
        if choice not in ('1','2','3','4'):
            raise ValueError("Invalid choice")
        x = float(input("Enter the first number:"))
        y = float(input("Enter the second number:"))
        
        if choice == '1':
            print(f"Addition of {x} and {y} = ",add(x,y))
        elif choice == '2':
            print(f"Subtraction of {x} and {y} = ",sub(x,y))
        elif choice == '3':
            print(f"Multiplication of {x} and {y} = ",mul(x,y))
        elif choice == '4':
            print(f"Division of {x} and {y} = ",div(x,y)) 
        
    except ZeroDivisionError as z:
        print("Error: ",z)
    except ValueError as e:
        print("Error: ",e)
    except Exception:
        print("Please Enter Valid number")
    
calculator()
    
    