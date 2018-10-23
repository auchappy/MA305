Script started on Tue 23 Oct 2018 09:51:09 AM EDT
piers@Lenovoman-G50-45:~/Documents/MA305/lab5$ cat lab5a.py
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

piers@Lenovoman-G50-45:~/Documents/MA305/lab5$ python3.lab5.py < dat5a.txt > out.

piers@Lenovoman-G50-45:~/Documents/MA305/lab5$ cat out.txt
['20050212   8	 15.30	  5.40\n', '20060212  12   14.50    9.52\n', '20070212	 8   16.30    6.40\n', '20080212  12   13.50	8.52\n', '20090212  12	 12.50	 -7.52\n']
['20050212', '8', '15.30', '5.40']
['20060212', '12', '14.50', '9.52']
['20070212', '8', '16.30', '6.40']
['20080212', '12', '13.50', '8.52']
['20090212', '12', '12.50', '-7.52']
===============================================
X Average: 14.42	 Y Average:  4.46	 Dot: 346.00

piers@Lenovoman-G50-45:~/Documents/MA305/lab5$ exit
exit

Script done on Tue 23 Oct 2018 09:51:58 AM EDT
