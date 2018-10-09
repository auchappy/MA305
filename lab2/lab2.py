#!/user/bin/env python3
"""

MA305 - Lab 2 : Piers Chapman -02OCT18 
Purpose: Evaluate the root of an inputted number.

"""
from math import *
#Receive Input
p=float(input('Number to find Sq. Root of:'))
xnew=float(input('Guess:'))
while(xnew<=0):
	xnew=float(input('Guess > 0:'))

#Compute root
xold=xnew
tol = 5*10**-15
i=0
while(True):
	xnew=(xold+(p/xold))/2
	abs_err_1 = abs(xold - xnew)
	abs_err_2 = abs((xold- xnew)/xnew)
	if(abs_err_1 < tol and abs_err_2 < tol ):
		break
	else:
		xold=xnew
		i=i+1
		print('',i,'',xnew,'%.6f' % abs_err_1,'%.6f' % abs_err_2)

