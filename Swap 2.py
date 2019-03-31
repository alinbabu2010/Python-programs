a,b=map(int,raw_input("Enter the numbers\n").split())
print("Values of a and b\n{0} {1}").format(a,b)
a=a+b
b=a-b
a=a-b
print("Swapped values of a and b\n{0} {1}").format(a,b)
