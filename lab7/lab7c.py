#!usr/bin/env python3
"""
==============================
Chapman, Piers - 05NOV18
Purpose: Use madhava formula to determine pi
==============================
"""
from math import *

def madhava(n):
	sum = 1
	for i in range(1,n):
		if i%2==0:
			sum += (1/((3+(2*(i-1)))*(3**i)))
		if i%2==1:
			sum -= (1/((3+(2*(i-1)))*(3**i)))
	return sum * sqrt(12)

print('n      madhava(n)    |math.pi-madhava(n)|')
for i in range(1,31):
	mad = madhava(i)
	print('{0:2d}    {1:2.10f}      {2:10.5f}'.format(i,mad,pi-mad))
