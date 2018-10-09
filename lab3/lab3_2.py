#!/user/bin/env python3
"""

MA305 - Lab 3_2 : Piers Chapman -08OCT18 
Purpose: Utilise the Luhn Algorithm to validate a credit card number
"""
from math import *

#Receive Input
#n = input('n=')
n = '1234567891234567'

#Reverse function
def rev(num):
	#rev = num.split(' ')
	rev = list(num)
	rev.reverse()	
	return rev

#Performs doubling on even elements within the array and sums > 9
def double(array):
	for i in range(len(array)):
		if(i%2==0):
			array[i] = int(array[i])
		else:
			test = int(array[i])*2
			if(test>9):
				#print(test)
				test2 = [int(x) for x in str(test)]
				#print(test2)
				#print(sum(test))
				array[i] = sum(test2)
			else:
				array[i] = test	
	return array

#Sums the entire array, which i realise is a function already in python now so this wasn't neccesary
def sum(array):
	sum=0
	for i in range(len(array)):		
		sum = array[i] + sum
	return sum 		
#Takes the modulus of the input by 10 and returns whether it's valid or not
def det(x):
	if(x%10 == 0):
		print('Valid Card Number')
	else:
		print('Invalid Card Number')	


det(sum(double(rev(n))))
