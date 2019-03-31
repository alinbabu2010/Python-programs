def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
n=input("Enter the number\n")
j=n
if n==0:
    print"Factorial of 0 is 1"
elif n>0:
        print"Factorial of a {0} is {1}".format(j,fact(n))
