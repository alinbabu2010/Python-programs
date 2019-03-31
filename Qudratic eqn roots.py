import math
a,b,c=map(int,raw_input("Enter the three coefficents of quadratic equation").split())
d=math.sqrt((b*b)-(4*a*c))
r1=(-b+d)/(2*a)
r2=(-b-d)/(2*a)
print("The roots of the equation are {} and {}").format(r1,r2)
