import math
def add():
    a,b=map(int,raw_input("Enter the two numbers\n").split())
    c=a+b
    print("Sum is {}").format(c)
def sub():
    a,b=map(int,raw_input("Enter the two numbers\n").split())
    c=a-b
    print("Difference is {}").format(c)
def pro():
    a,b=map(int,raw_input("Enter the two numbers\n").split())
    c=a*b
    print("Product is {}").format(c)
def div():
    a,b=map(int,raw_input("Enter the two numbers\n").split())
    c=a/b
    print("Quotient is {}").format(c)
def squt():
    a=input("Enter the number\n")
    c=math.sqrt(a)
    print("Square root of {0} is {1}").format(a,c)
def pwr():
    a,b=map(int,raw_input("Enter the number and power\n").split())
    c=pow(a,b)
    print("Power is {0}").format(c)

    
