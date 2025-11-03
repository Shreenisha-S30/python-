def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b != 0:
        return a/b
    else:
        return "cannot divisible by zero"
print("Addition: ",add(10,5))
print("subtraction: ",sub(10,5))
print("multiplication: ",mul(10,5))
print("division: ",div(10,5))