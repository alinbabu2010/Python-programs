l=input("Enter the limit\n")
i=0
lag=0
print("Enter the number one by one")
while(i<l):
      n=input("")
      if(n>lag):
          lag=n
      i=i+1
print("The largest number is {}").format(lag)    
    
