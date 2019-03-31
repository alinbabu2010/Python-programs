n=input("Enter the number\n")
s=0
t=k=n
c=0
while(k!=0):
     k=k/10
     if(k>=0):
         c=c+1
while(t!=0):
    r=t%10
    s=s+pow(r,c)
    t=t/10
if(n==s):
    print("Nummber is an armstromg number\n")
else:
    print("Nummber is not an armstromg number\n")
    

