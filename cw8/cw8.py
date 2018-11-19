#!/usr/bin/env python 
from math import *
from mySums import *
from myfuns import *

a=0.0
b=1.0 
n=int(input('Enter the number of rectangles n:'))
h=(b-a)/n 

print()
print("  i          xi          f(xi)   ")
left_sum = lsum(f,a,n,h)
exact=2
print()
print("Left-Sum Approximation:",left_sum)
abs_error=abs(left_sum-exact)
print ("        Absolute Error:",abs_error) 
print()

mid_sum = msum(f,a,n,h)
print()
print("Mid-Sum Approximation:",mid_sum)
abs_error=abs(mid_sum-exact)
print ("        Absolute Error:",abs_error) 
print()

right_sum = rsum(f,a,n,h)
print()
print("Right-Sum Approximation:",right_sum)
abs_error=abs(right_sum-exact)
print ("        Absolute Error:",abs_error) 
print()
#rel_error=100*abs(left_sum-exact)/abs(exact)
#print ("Relative Percentage Error:",rel_error) 


