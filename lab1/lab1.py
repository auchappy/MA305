#!/user/bin/env python3
"""

MA305 - Lab 1 : Piers Chapman -06SEP18 
Purpose: To evaluate F(x) = a-b*(x**3) at N equidistant points in [0,1], and output the pairs (x, F(x)) on the screen and in the file "out.txt" for plotting.

"""
#Get input from the user:
print('Please enter the values of a, b and N:')
a=input('a=')
b=input('b=')
N=input('N=')

#Print on screen:
print('\n Thanks, will run with: a=',a,', b=',b,', N=',N) 
print()
print(' #	x	F(x)')

#Change string input into number types:
a=float(a)
b=float(b)
N=int(N)

#Open a file (out.txt) for output:
out=open('out.txt','w') 
print(' #	x	F(x)', file = out)

# Compute F(x) = a-b*(x**3) and print x F(x)
dx=1/(N-1)
for i in range(N):
	xi = i*dx
	Fi = a-b*xi**3
	print('{0: 0.7f} {1: 0.7f}'.format(xi,Fi))
	print('{0: 0.7f} {1: 0.7f}'.format(xi,Fi),file=out)
out.close()

# Exit
print('\n All done, have a gday now!\n')
