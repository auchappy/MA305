#!/user/bin/env python3
"""

MA305 - Classwork 4 : Piers Chapman -06OCT18 
Purpose: Practice for loops and control flows in Python

"""
from math import *

n = int(input('n='))
#Geometric Series
def geoSeries(n):
	sum = 1
	for i in range(1,n):
		sum=sum+(1/2**i)
		print("GeoSum:",sum)
	return sum	

#Harmonic Series
def harSeries(n):
	sum=0
	for i in range(1,n):
		sum=sum+(1/i)
		print("HarSum:",sum)
	return sum

#Alternating Series
def altSeries(n):
	sum=0
	for i in range(1,n):
		sum=sum+((-1)**((i+1))/i)
		print("AltSum:",sum)
	return sum

print("Geo:",geoSeries(n))
print("Har:",harSeries(n))
print("Alt:",altSeries(n))


