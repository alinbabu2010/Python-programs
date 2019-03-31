n=input("Enter the number\n")
a=0
b=1
i=1
print("Fibonocci series upto {0} :".format(n))
print a,b, 
for i in range(1,n-1):
    c=a+b
    print c,
    a=b
    b=c
