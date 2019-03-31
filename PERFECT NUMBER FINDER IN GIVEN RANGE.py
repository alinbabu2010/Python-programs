print"\t\t\tPERFECT NUMBER FINDER IN GIVEN RANGE\n\n\n"
def factor(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if s==n:
        print n,
r,f=map(int,raw_input("Enter the range to find perfect numbers\n").split())
print"\nPerfect numbers in range {} - {} :".format(r,f)
for j in range(r,f):
    factor(j)

