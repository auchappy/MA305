#!/user/bin/env python3
"""

MA305 - Lab 3 : Piers Chapman -08OCT18 
Purpose: To deterine the hailstone sequence starting at integer 'n'
"""
from math import *

#Receive Input
n = int(input('n='))
count=0
#Compute Hailstone Sequence

while(n !=1):
	if(n%2==0):
		n = n/2
	else:
		n = 3*n+1
	count=count+1	
print('Hailstone Sequence has:',count,'numbers')
