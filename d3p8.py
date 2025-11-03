while True:
    print("\nSimple calculator")
    print("Select operation:")
    print("1.Add")
    print("2.sub")
    print("3.Mul")
    print("4.Div")
    print("5.Exit")
    choice=int(input("Enter the choice (1/2/3/4/5): "))
    a= int(input("Enter the num1: "))
    b= int(input("Enter the num2: "))
    if choice== 1:
        print("Result: ",a+b)
    elif choice== 2:
        print("Result: ",a-b)
    elif choice== 3:
        print("Result: ",a*b)
    elif choice== 4:
        if b != 0:
            print("Result: ",a/b)
        else:
            print("Result: a cannot divisible by b!")
    elif choice== 6:
        print("Thankyou goodbye!😊")

    else:
        print("Invalid number, please enter valid number.\n ")
        break


