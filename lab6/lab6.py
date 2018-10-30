#!/usr/bin/env python3
import sys
"""
==========================================
MA305 - LAB 6: CHAPMAN, PIERS - 29OCT18
PURPOSE: Read data into arrays enabling extraction of information.
==========================================
"""

f = open('data6.txt','r')
f.readline()
data = f.readlines()

D = []
T = []
H = []

#Begin functions
def max(listIn = [] ):
	oldMax = 0
	newMax = 0
	for i in range(len(listIn)):
		newMax = int(listIn[i])
		if (newMax > oldMax):
			oldMax = newMax
	return oldMax

def min(listIn = []):
	oldMin = 0
	newMin = 0
	for i in range(len(listIn)):
		newMin = int(listIn[i])
		if (newMin < oldMin):
			oldMin = newMin
	return oldMin

def avg(listIn = []):
	temp = []
	for i in range(len(listIn)):
		temp.append(int(listIn[i]))
	avg = sum(temp) / len(listIn)
	return avg

def heat_index(T,H):
	if(T > 55):
		HI = -42.379 + 2.04901523*T + 10.14333127*H - 0.22475541*T*H - 6.83783e-3*T*T - 5.481717e-2*H*H + 1.22874e-3*T*T*H + 8.5282e-4*T*H*H - 1.99e-6*T*T*H*H 
	else:
		HI = T
	return HI

#Begin code
for line in data:
	Linelist = line.split()
	D.append(int(Linelist[0]))
	T.append(int(Linelist[1]))
	H.append(int(Linelist[2]))
	print(Linelist)
f.close()
print('==========================================')
cBelow = 0
cAbove = 0
avgT = avg(T)
avgH = avg(H)
for i in range(len(T)):
	if (T[i] < 0):
		cBelow+=1
	if (T[i] > avgT):
		cAbove+=1

date = []
for i in range(len(D)):
	day = (int(D[i])%100)
	month = (((int(D[i]))//100)%100)
	year = (int(D[i]//10000))

#	date append(month,'/',day,'/',year)

for i in range(len(T)):
	temp = int(T[i])
	hum = int(H[i])
	hi = heat_index(temp,hum)
	print('Temp: {0:-5.0f}\tHumidity: {1:-5.0f}\tIndex: {2:-5.0f}'.format(temp,hum,hi))
