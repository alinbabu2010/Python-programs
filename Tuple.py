n=input("Enter the limit\n")
t=[]
print"Enter the strings in tuples"
for i in range(0,n):
    t.insert(i,raw_input(""))
s=tuple(t)    
print s
c=0
k=raw_input("Enter a string to match\n")
for i in s:
    w=i
    if k in w:
        c=c+1
print"The count of pattern in tuple:"
print c
