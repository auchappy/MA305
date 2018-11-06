#!usr/bin/env python3
"""
==============================
Chapman, Piers - 05NOV18
Purpose: Calculate pi using the trapezoidal rule
==============================
"""
from math import *

def f(x):
	#return 2*x
	#return 3*(1-x**2) 
	#return 4*sqrt(1-x**2)
	return 2/(1+x**2)

def trapezoidal(f,a,b,n):
	h = (b-a)/n
	trap_sum = f(a) + f(b)
	for i in range (1,n-1):
		xi = a + i*h
		fi = f(xi)
		trap_sum += 2*fi 
	return (h/2)*trap_sum

a = float(input('Lower Bound a:'))
b = float(input('Upper Bound b:'))
m = int(input('Please enter m, where i = 2^m:'))
print("  m            N             T             error")
I = pi

for i in range(5,m+1):
	T = trapezoidal(f,a,b,2**i)
	error = abs((T-I)/I)
	print('{0:3d}\t{1:10.1f}\t{2:10.10f}\t{3:2.10f}'.format(i,2**i,T,error))
