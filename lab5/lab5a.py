#!/usr/bin/env python3 
import sys

"""
========================================================================
MA305 - Lab 5: Chapman, Piers - 22OCT18
Purpose: . . . 
======================================================================== 
"""
#f = open('dat5a.txt','r')
f = sys.stdin
f.readline()
data=f.readlines()
print(data)
x=[]
y=[]
n=0
for line in data:
	n+=1
	Linelist = line.split()
	x.append(float(Linelist[2]))
	y.append(float(Linelist[3]))
	print(Linelist)
f.close()
print('===============================================')
sx=sy=0
dot=0.0
for i in range(n):
	sx += x[i]
	sy += y[i]
	dot += x[i]*y[i]
x_avg = sx/len(x)
y_avg = sy/len(y)
print('X Average: {0:-5.2f} \t Y Average: {1:-5.2f} \t Dot: {2:-5.2f}'.format(x_avg,y_avg,dot))
print()

