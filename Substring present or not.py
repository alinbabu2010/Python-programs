def sub(s,u):
    i=j=c=0
    a=len(s)
    b=len(u)
    while i<a:
        while j<b:
            if s[i]==u[j]:
                j=j+1
                if j==b:
                    c=c+1
                    k=j
                    j=0
            else:
                break
        i=i+1
    if k==b:
        print"Sub string present"
    else:
        print"Sub string not present"
    return c
s=raw_input("Enter the string\n")
u=raw_input("Enter the sub string\n")
h=sub(s,u)
print"Number of times sub string present : {}".format(h)
