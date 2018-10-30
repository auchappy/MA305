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
def max(listIn = []):
        oldMax = listIn[0]
        newMax = 0
        index  = 0     
        for i in range(1,len(listIn)):
                newMax = listIn[i]
                if (newMax > oldMax):
                        oldMax = newMax
                        index = i      
        return oldMax, index

def min(listIn = []):
        oldMin = listIn[0]
        newMin = 0
        index  = 0
        for i in range(len(listIn)):
                newMin = listIn[i]
                if (newMin < oldMin):
                        oldMin = newMin
                        index = i      
        return oldMin, index

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

def date(x):
        day   = (x%100)
        month = (x//100)%100
        year  = (x//10000)
        return day, month, year


#Begin code
for line in data:
        Linelist = line.split()
        D.append(int(Linelist[0]))
        T.append(int(Linelist[1]))
        H.append(int(Linelist[2]))
        #print(Linelist)
f.close()
print('=================Data Print=================')
cBelow = 0
cAbove = 0
avgT = avg(T)
avgH = avg(H)
HI = []
for i in range(len(T)):
        if (T[i] < 32):
                if(T[i] > 0):
                        cBelow+=1
        if (T[i] > 50):
                cAbove+=1
        HI.append(heat_index(T[i],H[i]))       

for i in range(len(T)):
        day, month, year = date(D[i])
        temp = int(T[i])
        hum = int(H[i])
        hi = heat_index(temp,hum)
        print('Date: {0:2}/{1:2}/{2:2}\tTemp:{3:3}\tHumidity:{4:2}\tIndex:{5:6.2f}'.format(month,day,year,temp,hum,hi))
print('============================================')

#lowest temperature
tMin, tMinIndex = min(T)
tMinDay, tMinMonth, tMinYear = date(D[tMinIndex])
heatIndexDay = HI[tMinIndex]
humDay = H[tMinIndex]
print('Date: {0:2}/{1:2}/{2:2}\tTemp:{3:3}\tHumidity:{4:2}\tIndex:{5:6.2f}\tLowest Temperature'.format(tMinMonth,tMinDay,tMinYear,tMin,humDay,heatIndexDay))

#max heat_index
hiMax, hiMaxIndex = max(HI)
hiMaxDay, hiMaxMonth, hiMaxYear = date(D[hiMaxIndex])
tempHIMax = T[hiMaxIndex]
humHIMax = H[hiMaxIndex]
print('Date: {0:2}/{1:2}/{2:2}\tTemp:{3:3}\tHumidity:{4:2}\tIndex:{5:6.2f}\tHighest Heat Index'.format(hiMaxMonth,hiMaxDay,hiMaxYear,tempHIMax,humHIMax,hiMax))

#break
print('============================================')

#averages
avgHI = avg(HI)
print('Average Temperature:{0:3}\tAverage Humidity:{1:2}\tAverage Heat Index:{2:6.2f}'.format(avgT,avgH,avgHI))
print('Days below 32:{0:3}\tDays above 50:{1:3}'.format(cBelow,cAbove))