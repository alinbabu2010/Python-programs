def fib(n1):
    if n1==1:
        return n1
    elif n1==0:
        return n1
    else:
        return fib(n1-1)+fib(n1-2)
n=input("Enter the limit\n")
print("The fibonocci series upto {} :").format(n)
i=0
while(i<=n):
    k=fib(i)
    print k
    i=i+1
