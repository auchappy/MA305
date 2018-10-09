#!/user/bin/env python3
"""

MA305 - Lab 2 : Piers Chapman -02OCT18 
Purpose: To determine Gauss's constant of two numbers inputted by the user.
"""
from math import *
#Receive Input
xnew = float(input('x='))
ynew = float(input('y='))

#Compute root
xold=xnew
yold=ynew
tol = 5*10**-15
i=0

while(True):
	xnew = 0.5*(xnew+ynew)
	ynew = sqrt(xnew*ynew)
	abs_err_x = abs(xold - xnew)
	abs_err_y = abs(yold - ynew)
	if(abs_err_x < tol and abs_err_y < tol):
		print('G = {:.6f}'.format(1/xnew))
		break
	else:
		xold=xnew
		yold=ynew
		i=i+1
		print('',i,'',xnew,'',ynew)
