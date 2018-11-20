#!usr/bin/env python3
"""
=====================================
Chapman, Piers - 15NOV18
Purpose: Use a matrix to determine the 1-, infinite, and Frobenious norms. 
=====================================
"""

import numpy as np
import time as clock

start = clock.time()

def froben(trix):
	shape = trix.shape
	row = shape[0]
	col = shape[1]
	frob = 0
	for m in range(row):
		for n in range(col):
			frob+=trix[m,n]**2

	frob = np.sqrt(frob)
	return frob

def norm(trix):
	shape = trix.shape
	row = shape[0]
	col = shape[1]
	inf = 0
	for i in range(row):
		count = 0
		for j in range(col):
			count+=trix[i,j]
		if (count>inf):
			inf = count
	return inf

def infinite(trix):
	shape = trix.shape
	row = shape[0]
	col = shape[1]
	first = 0
	for i in range(col):
		count = 0
		for j in range(row):
			count+=trix[j,i]
		if(count>first):
			first = count
	return first

A = np.fromfunction(lambda x,y : 2*x+y, (4,5))
B = A.transpose()
C = A.dot(B)
#print(A)
#print(B)
#print(C)
print()
print('     Frobenious for C:    {0:10.5f} Norm:    {1:10.5f} Infinite:    {2:10.5f}'.format(froben(C),norm(C),infinite(C)))
matrix = np.fromfunction(lambda x,y : 2*x+y, (1000,1000))
print('Frobenious for Matrix: {0:10.5f} Norm: {1:10.5f} Infinite: {2:10.5f}'.format(froben(matrix),norm(matrix),infinite(matrix)))
print()
print('Code Run Time:',clock.time() - start)
