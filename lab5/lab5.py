#!/usr/bin/env python3 

"""
========================================================================
MA305 - Lab 5: Chapman, Piers - 22OCT18
Purpose: . . . 
======================================================================== 
"""

f = open('dat5.txt','r')
line = f.readline()
print(line,end='') # end='', forces not to print and extra blank line
n=0
x = []
y = []

while  True:
	n=n+1
	line = f.readline()
	Linelist = line.split()
	x.append(float(Linelist[2]))
	y.append(float(Linelist[3]))
	if int(Linelist[0])==0:
		break
	print(Linelist)
	print('\t {0:-5.2f} \t{1:-5.2f}'.format(float(Linelist[2]),float(Linelist[3])))
f.close()
print(n,"lines from 'dat5.txt' are read for calculations!")
#####
print('=====================================')
sx = sy = 0
for i in range (n):
	sx +=x[i]
	sy +=y[i]
print('  Sum: : {0:-5.2f} \t {1:-5.2f}'.format(sx,sy))
print()
