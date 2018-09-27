#!/user/bin/env python3
"""
MA305 - Classwork 3: Piers Chapman 25SEP18
Purpose: Evaluate the Euler's funtion of a integer 'n' that is inputted.
"""
"from math import *"

#Define GCD function
def gcd(a,b):
	while b:
		a, b = b, a%b
	return a

#Define Phi Function
def phi(n):
	list=[]
	result = 0
	for i in range(2,n):
		if (gcd(i,n) == 1):	
			list.append(i)
	return (list)

n = int(input('n='))
list = phi(n)
count = len(list)

print('There are',count,'integers relatively prime to',n,'less than ',n)
print(list)
