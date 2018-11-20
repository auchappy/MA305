#!usr/bin/env python3
"""
==============================
Chapman, Piers - 15NOV18
Purpose: Takes an array and computes sum, product, min, max , avg, variance and standard deviation
==============================
"""

import numpy as np
from math import *


#Functions
def x_mean(x):
	summ = 0
	for i in range(len(x)):
		summ += x[i]
	return summ/len(x)

def x_var(x):
	varr = 0
	for i in range(len(x)):
		varr += x[i]**2
	varr = varr/len(x)
	varr -= x_avg(x)**2
	return varr

def x_prod(x):
	prod = 1
	for i in range(0,len(x)):
		prod *= x[i]
	return prod

def greaterThanAvg(x,y):
	greaterCount = 0
	for i in range(len(x)):
		if (x[i] > y):
			greaterCount+=1
	lesserCount = len(x) - greaterCount
	return greaterCount, lesserCount

rand_x = np.random.rand(15)

#for i in range(0,len(rand_x),5):
#	print('{0:2.3f}\t{1:2.3f}\t{2:2.3f}\t{3:2.3f}\t{4:2.3f}'.format(rand_x[i],rand_x[i+1],rand_x[i+2],rand_x[i+4],rand_x[i+4]))

#NumPy Calculations
xavg = np.mean(rand_x)
xsumm = np.sum(rand_x)
xprod = x_prod(rand_x)#np.prod(rand_x)
xvar = np.var(rand_x)
xstd = np.std(rand_x)
xmax = np.max(rand_x)
xmax_loc = np.argmax(rand_x)
xmin = np.min(rand_x)
xmin_loc = np.argmin(rand_x)

#print(rand_x)
print()

print('              i             x')
for i in range(len(rand_x)):
	print('             {0:2d}         {1:5.5f}'.format(i,rand_x[i]))
print('=========================================')
print('X Sum:{0:3.5f} X Avg:{1:3.5f} X Prod:{2:3.5f}e-6'.format(xsumm,xavg,xprod*10**6))
print('     X Max:{0:3.5f} X Max Loc:{1:2d}'.format(xmax,xmax_loc))
print('     X Min:{0:3.5f} X Min Loc:{1:2d}'.format(xmin,xmin_loc))
print('=========================================')

sort_x = sorted(rand_x)
rev_x = sorted(rand_x, reverse=True)
print('     Low to High      High to Low')
for i in range(len(rand_x)):
	print('\t{0:3.5f}\t\t{1:3.5f}'.format(sort_x[i],rev_x[i]))
print()
countAbove, countBelow = greaterThanAvg(rand_x,xavg)
medAbove, medBelow = greaterThanAvg(rand_x,np.median(rand_x))
print('{0:2d} numbers below average of {1:1.5f} and {2:2d} above'.format(countBelow,xavg,countAbove))
print('{0:2d} numbers below median of {1:1.5f} and {2:2d} above'.format(medBelow,np.median(rand_x),medAbove))
