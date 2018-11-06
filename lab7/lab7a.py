#!usr/bin/env python3
"""
==============================
Chapman, Piers - 05NOV18
Purpose: Use the trapezoidal rule to approximate the area of a curve
==============================
"""
from math import *

def f(x):
	return 2*x
	#return 3*(1-x**2) 

def trapezoidal(f,a,b,n):
	h = (b-a)/n
	trap_sum = f(a) + f(b)
	print('  i\t\txi\t    f(xi)')
	for i in range (1,n-1):
		xi = a + i*h
		fi = f(xi)
		trap_sum += 2*fi 
		print('{0:3d}\t{1:10.5f}\t{2:10.5f}'.format(i,xi,fi))
	return (h/2)*trap_sum

a = float(input('Lower Bound a:'))
b = float(input('Upper Bound b:'))
n = int(input('Number of trapezoids n:'))

exact = f(b)-f(a)
approx = trapezoidal(f,a,b,n)
error1 = abs(approx-exact)
print("N=",n)
print('                \tApproximation\tError')
print('Trapezoidal-Sum:\t{0:12.10f}\t{1:12.10f}'.format(approx,error1))
