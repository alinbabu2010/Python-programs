def pal(n):
    t=n
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n/10
    if(t==s):
        print"Palindrome"
    else:
        print"Not palindrome"    
n=input("Enter a number\n")
pal(n)
