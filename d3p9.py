#simple calculator

def add(a,b):
    return a+b

def diff(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "undifined"
    else:
        return a/b
while True:
    print("\n--SELECT OPERATION--")
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice = input("Enter your choice:")
  
    match choice:
        case '1':
            a = int(input("Enter the 1st operand:"))
            b = int(input("Enter the 2nd operand:"))
            print(f"\nthe sum of {a} and {b} is {add(a,b)}")
            
        case '2':
            a = int(input("Enter the 1st operand:"))
            b = int(input("Enter the 2nd operand:"))
            print(f"\nthe difference of {a} and {b} is {diff(a,b)}")

        case '3':
            a = int(input("Enter the 1st operand:"))
            b = int(input("Enter the 2nd operand:"))
            print(f"the product of {a} and {b} is {mult(a,b)}")

        case '4':
            a = int(input("Enter the 1st operand:"))
            b = int(input("Enter the 2nd operand:"))
            print(f"the quotient of {a} and {b} is {div(a,b)}")
        case '5':
            print("Thank you!!")
            break
        case _:
            print("invalid choice")