#!/usr/bin/env python3 
"""
========================================================================
MA305 - cw7: your name - date
Purpose: revisit bisection code ... using modules ... 
========================================================================
"""

# Define functions here:
def F(x): 
    value = - 3. + x * ( -3. + x * ( 1. + x ) ) #=x**3+x**2-3.0*x-3.0 
    return value

def G(x): 
    value=1-2*x
    return value

def bisection(F, a, b, Nmax, Tol):
    #................ Find values at endpoints:
    Fa = F(a)
    Fb = F(b)
    #................ Initialization:
    print('  n            r             F(r)           error')
    n = 0 # initialize the counter
    error = abs(b-a) # initialize the error
    #---------------- Begin Bisection Loop ---------------
    for n in range(1,Nmax):
        r = ( a + b ) / 2
        Fr = F(r)
        if( Fr == 0 ):
            print('Got lucky! root =',r,' F(r)=',Fr)
            print(' in',n,' tries',' error <=',error/2)
            break
        elif( Fa * Fr < 0 ):
            b =  r
            Fb = Fr
        else:
            a =  r
            Fa = Fr   
            error = error/2 # or: = b-a
            # print this iterate
            print('{0:3d} {1: 15.8g} {2: 15.8g} {3: 15.8g}'.format(n,r,Fr,error)) 
            if( error < Tol ): 
                exit()
            if( n > Nmax ):
                print('....NOT done, iterations exhausted:')   
                print(' n=',n,' > Nmax=',Nmax)
                print('try shorter [a,b], or bigger nMAX; Exiting...')
                exit()
    #---------------- end of bisection loop ---------------
    return r

if __name__ == '__main__':
        
# Get input from user and change the string input into number types: 
    print(' Enter the interval, Max iteration and Tolerance')    
    a,b,Nmax,Tol=input(' a, b, Nmax, Tol:').split() 
    a=float(a)
    b=float(b)
    Nmax=int(Nmax)
    Tol=float(Tol)
    # Print on screen: 
    print('\n Searching for root in [{0: 5.2f}, {1: 5.2f}], with TOL={2:0.8g}'.format(a,b,Tol))
    print('-------------------------------------------------------')
    r = bisection(F, a, b, Nmax, Tol) 
    print('-------------------------------------------------------')
    print('Done! best estimate for the root:{0: 21.14g}'.format(r))
    print()
    
