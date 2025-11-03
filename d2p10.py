#write a python program to  print square pattren 
n=int(input("Enter the num: "))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
"""output : * * * * *
            * * * * *
            * * * * *
            * * * * *
            * * * * * """


n=int(input("Enter the number:"))
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()

#output: *
#        * *
#        * * *
#        * * * *
#        * * * * *
rows =5
for i in range(1,rows+1):
    print("*" *i)

#another pattren 
n=int(input("Enter the number:"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
    
#..........
rows =5
for i in range(rows,0,-1):
    print("*" * i)