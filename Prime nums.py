n=input("Enter the number\n")
i=2
j=1
print("The prime number upto {0} are\n".format(n))
for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        if(i%j==0):
            count=count+1
            j=j+1
    if(count==2):
        print i
        i=i+1
        

    
