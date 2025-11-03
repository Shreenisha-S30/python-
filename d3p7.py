print("Simple calculator")
print("Select operation:")
print("\n1.Add")
print("\n2.sub")
print("\n3.Mul")
print("\n4.Div")
print("\n5.Exit")
choice=int(input("Enter the choice (1/2/3/4/5): "))
a= int(input("Enter the num1: "))
b= int(input("Enter the num2: "))
match choice:
    case 1:
        print("Result: ",a+b)
    case 2:
        print("Result: ",a-b)
    case 3:
        print("Result: ",a*b)
    case 4:
        if b != 0:
            print("Result: ",a/b)
        else:
            print("Result: a cannot divisible by b!")
    case 5:
        print("Thankyou goodbye!😊")

    case _:
        print("Invalid number, please enter valid number ")
        


