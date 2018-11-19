#!/usr/bin/env python 
from myfuns import f
from  mySums import *


a=0.0
b=1.0 
n=int(input('Enter the number of rectangles n:'))

exact=2

for i in range(5,n):
    N=2**i
    approx1=lsum(f,a,b,N)
    approx2=rsum(f,a,b,N)
    approx3=msum(f,a,b,N)

    error1=abs(approx1-exact)
    error2=abs(approx2-exact)
    error3=abs(approx3-exact)

    print("N=",N)
    print("                 Approximation       Error")
    print("  Left-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx1, error1))
    print(" Right-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx2, error2))
    print("   Mid-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx3, error3))
    print()



