num=int(input("Enter the Interger number:"))
if num==0:
    print(f"{num} is neither even nor odd(zero)")
elif num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")