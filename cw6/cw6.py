#!/usr/bin/env python3 
import sys
"""
========================================================================
MA305 - cw 6: your name - date
Purpose: Reading and arrays from a date file and calculate the average
========================================================================
"""

def calc_average(x):
    n=len(x)
    s=0 
    for i in range (n): 
        s += x[i] 
    xave=s/n    
    return xave

def locate_max(x):
    n=len(x)
    xmax=x[0]
    loc=0
    for i in range(1,n): 
        if (x[i]>xmax): 
            xmax=x[i]
            loc=i
    return xmax, loc

def myfunction(x,y): #f(x,y) = 2x+y
    n=len(x) 
    z=[]
    for i in range(n): 
        value=2*x[i] + y[i]
        z.append(value)
    return z 

def dd_mm_yyyy(Date): 
    day=Date%100
    month=(Date//100)%100
    year=Date//10000 
    return day, month, year 

#dat = input('Enter the name of the file to read data from:') 
#f = open(dat,'r') 

f=sys.stdin 

header=f.readline() 
print(header,end='')
n=0
D=[]
X=[]
Y=[]
 
for line in f.readlines():
    Line = line.split() 
    print(Line)
    D.append(int(Line[0]))
    X.append(float(Line[2]))
    Y.append(float(Line[3]))
    n += 1 
f.close() 

print() 

print('=================================')
print('    D         X       Y     Z')
Z = myfunction(X,Y) 
for i in range(n): 
    print('{0: 8d}  {1:-6.2f}  {2:-6.2f}   {3:-6.2f}'.format(D[i],X[i],Y[i], Z[i]))

print('=================================')

print() 
Zave = calc_average(Z) 
print(' Z average:',Zave)
print() 
Zmax, Zmaxloc = locate_max(Z) 
print(' Zmax:',Zmax)

day, month, year = dd_mm_yyyy(D[Zmaxloc]) 
print(' Date for Zmax: {1:02d}/{0:02d}/{2:04d}'.format(day,month,year))
print() 



