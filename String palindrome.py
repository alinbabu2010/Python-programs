s=raw_input("Enter the string\n")
k=len(s)
r = ""
for c in s:
    r = c + r
b=0
for i in range(0,len(r)):
    if r[i]==s[k-1]:
        b=b+1
        k=k-1
    else:
        k=k-1
if b==len(r):
    print"Palindrome"
else:
    print"Not palindrome"


