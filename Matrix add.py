n=input("Enter the no: of matrices you want to add\n")
g=[]
for t in range(0,n):
    r=input("Enter the no: of rows\n")
    c=input("Enter the no: of columns\n")
    m=[]
    for i in range(0,r):
        l=[]
        for j in range(0,c):
            k=input()
            l.insert(j,k)
        m.insert(i,l)
    print"The list of matrix is:"
    print m
    g.insert(t,m)
print"The sum of matrices:"
for d in range(0,n):
    s=[]
    for e in range(0,r):
        v=0
        for f in range(0,c):
            v=v+g[f][e][d]
        s.insert(e,v)
print s
            
            
    
    
