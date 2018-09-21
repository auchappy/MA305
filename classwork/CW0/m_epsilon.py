#!/usr/bin/env python
import sys 
import numpy as np 
from math import log

# Machine epsilon calculation
eps = 1 
while (1+eps) != 1:
        eps = eps/2
eps = 2*eps

print ()
print ("           eps =",eps)

test_expression = abs(3*(4/3-1)-1)
print (" |3*(4/3-1)-1| =",test_expression)
print ()


# Machine epsilon in various arithmetic precision
for prec in ['16-bit', '32-bit', '64-bit', '128-bit']:
    if (prec == '16-bit'): 
        x = np.float16(4/3)
        y = np.float16(x-1)
        w = np.float16(3*y)
        z = np.float16(w-1)
    elif (prec == '32-bit'): 
        x = np.float32(4/3)
        y = np.float32(x-1)
        w = np.float32(3*y)
        z = np.float32(w-1)
    elif (prec == '64-bit'): 
        x = np.float64(4/3)
        y = np.float64(x-1)
        w = np.float64(3*y)
        z = np.float64(w-1)
    else: 
        x = np.float128(4/3)
        y = np.float128(x-1)
        w = np.float128(3*y)
        z = np.float128(w-1)
    eps = abs(z) 
    temp=log(eps)/log(2)
    print ( format(prec,'s'), " machine epsilon =", 
        format(eps, '0.21g'), "= 2^",format(int(temp),'d'))
    
print("sys.float_info.epsilon =", sys.float_info.epsilon) 
print ()





