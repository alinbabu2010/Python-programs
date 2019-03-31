a,b=map(int,raw_input("Enter the numbers\n").split())
c=raw_input("Enter the operator\n")
def add():
    s=a+b
    print("Sum = {}").format(s)
def difference():
    d=a-b
    print("Difference = {}").format(d)
def product():
    p=a*b
    print("Product = {}").format(p)
def quotient():
    q=a/b
    print("Quotient = {}").format(q)
if(c=='+'):
    add()
elif(c=='-'):
    difference()
elif(c=='*'):
    product()
else:
    quotient()
