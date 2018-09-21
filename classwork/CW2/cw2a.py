#!/user/bin/env python3
from math import *
"""

MA305 - Classwork 2: Piers Chapman 20SEP18
Purpose: To evaluate multiple expressions, such as the volume of a cylinder, resistance of 3 resistors and cos() of a function.

"""
#Set Variables
print('Please enter the values of r and h:')
r = float(input('r='))
h = float(input('h='))

#Calculate and display value
v = pi*((r/2)**2)*h
print('The volume of the cylinder is: ', v)

#Set Variables for Resistance
print('Please enter the values of r1, r2, and r3:')
r1 = float(input('r1='))
r2 = float(input('r2='))
r3 = float(input('r3='))

#Calculate resistance and display
res = 1/((1/r1)+(1/r2)+(1/r3))
print('The resistance of the three resistors is: ', res)

#Set variables for cos()
r = -0.3
theta = (3*pi)/4

#Calculate and display
y = (e**r)*cos(theta)+e**(2*r)*sin(2*theta)
print('Y is equal to: ',y)
