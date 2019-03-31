f1=open('orginal.txt','w')
f2=open('duplicate.txt','w')
st=raw_input("Enter a string\n")
f1.write(st)
f1.close()
f1=open('orginal.txt','r')
st1=f1.read()
print"The contents of orginal file:\n{}".format(st1)
f2.write(st1)
f2.close()
f1.close
f2=open('duplicate.txt','r')
s=f2.read()
print"Content in duplicate file:"
print s
f2.close()

