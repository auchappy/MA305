#!usr/bin/env python3
"""
==============================
Chapman, Piers - 05NOV18
Purpose: Use the trapezoidal rule to approximate the area of a curve
==============================
"""

import numpy as np
from matplotlib import pylab as plt

def datLoad(name):
	f = open(name)
	dat = f.readlines()
	datRet = []
	for line in dat:
		Line = line.split()
		for i in range(0,5):
			datRet.append(float(Line[i]))
	f.close()
	return datRet	 

male = datLoad('dataM.txt')
fmale = datLoad('dataF.txt')
mMean = np.mean(male)
mMed = np.median(male)
mDevi = np.std(male)
fMean = np.mean(fmale)
fMed = np.median(fmale)
fDevi = np.std(fmale)
fmale = datLoad('dataF.txt')

print('==========================================================')
print()
print('  Male Mean: {0:5.2f}cm Median: {1:5.2f}cm Deviation: {2:5.2f}cm'.format(mMean,mMed,mDevi))
print('   Male Max: {0:5.2f}cm    Min: {1:5.2f}cm'.format(np.max(male),np.min(male)))
print('Female Mean: {0:5.2f}cm Median: {1:5.2f}cm Deviation: {2:5.2f}cm'.format(fMean,fMed,fDevi)) 
print(' Female Max: {0:5.2f}cm    Min: {1:5.2f}cm'.format(np.max(fmale),np.min(fmale)))
print()
print('==========================================================')

np.histogram(male,bins=20,range=(np.min(male),np.max(male)))
np.histogram(fmale,bins=20,range=(np.min(fmale),np.max(fmale)))
plt.hist([male,fmale],bins=20,range=(120,220),label=['Male','Female'])
plt.legend(loc='upper right')
plt.savefig('plot.pdf')
pylab.show()


