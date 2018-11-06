#!usr/bin/env python3
"""
==============================
Chapman, Piers - 05NOV18
Purpose: Math
==============================
"""
from math import *

def f(x):
	return x**2
	
def trapezoidal(f,a,b,n):
	h = (b-a)/n
	trap = 0.5*(f(a)+f(b))
	for i in range (1,n):
		xi = a+i*h
		trap += xi
	return h*trap

exact = abs(f(b)-f(a))


