#write a python program to print fibonacci series without using temp variable
n=int(input("Enter the number of terms: "))
a=0
b=1
print("Fibonacci Series:")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

#write a python program to print fibonacci series using temp variable
n=int(input("Enter the number of terms: "))
a=0
b=1
print("Fibonacci Series: ")
for i in range(n):
    print(a,end=" ")
    temp=a+b
    a=b
    b=temp