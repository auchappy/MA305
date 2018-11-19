#!/user/bin/env python
'''
==============================================================
MA305 - CW8 : Piers Chapman - 29OCT18
Purpose: To determine the riemans sum of a function with relation to the number of 'boxes' utilised.
==============================================================
'''

def lsum(f,a,b,n):
	h = (b-a)/n
	left_sum = 0
	xi = a+i*h
	fi=f(xi)
	print('{0:3d}    {1:10.5f}   {2:10.5f}'.format(i,xi,fi))
	left_sum += h*fi
	return left_sum

def msum(f,a,b,n):
	h = (b-a)/n
	mid_sum = 0
	for i in range(n):
		xi = a+0.5*h+i*h
		fi=f(xi)
		print('{0:3d}    {1:10.5f}   {2:10.5f}'.format(i,xi,fi))
		mid_sum += h*fi
	return mid_sum

def rsum(f,a,b,n):
	h = (b-a)/n
	right_sum = 0
	for i in range(1,n+1):
		xi = a+i*h
		fi=f(xi)
		print('{0:3d}    {1:10.5f}   {2:10.5f}'.format(i,xi,fi))
		right_sum += h*fi
	return right_sum
