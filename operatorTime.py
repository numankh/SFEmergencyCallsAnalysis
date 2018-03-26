import csv
import collections
import datetime
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import math


def average(arg):
    total = 0
    for x in range(len(arg)):
        if not math.isnan(arg[x]):
            total += arg[x]
            
    return total/len(arg)

def outlier(arg):
    
    numOfOutliers = 0
    num = len(arg)
    arg = sorted(arg) #sorting the list
    mid = int(num/2)    #median value
    Q1 = int(mid/2)
    Q3 = mid + int(mid/2)
    
    for x in arg:
        print(arg)


    IQR = arg[Q3] - arg[Q1]
    LB = arg[Q1] - (1.5 * IQR)
    UB = arg[Q3] + (1.5 * IQR)

    
    print("OUTLIER < " + str(LB))
    print(str(UB) + "< OUTLIER")
    
    for x in range(num):
        if arg[x] > UB:
            numOfOutliers += 1
    
    print(num)
    print(numOfOutliers)
    
    
        
def standard_deviation(arg):
    num = len(arg)
    total = 0
    for x in range(len(arg)):
        if not math.isnan(arg[x]):
            total += arg[x]     
        
    if num < 2:     #if the list is shorter than 2
                    #then the stdv cannot be found
        return None
    else:
        sumavg = 0
        for x in range(len(arg)):
            if not math.isnan(arg[x]):
                 sumavg = sumavg + ((arg[x] - (total/num)) ** 2)
        return (sumavg/(num-1))**.5     #returns the stdv

fileName = "sfpd_dispatch_data_subset.csv"


df = pd.read_csv(fileName)
d0 = df['received_timestamp']
d1 = df['dispatch_timestamp']


delta = []


#date0 = datetime.datetime.strptime(d0[x], "%Y-%m-%d %H:%M:%S.%f %Z")
#date1 = datetime.datetime.strptime(d1[x], "%Y-%m-%d %H:%M:%S.%f %Z")

date0 = pd.to_datetime(d0, format = "%Y-%m-%d %H:%M:%S.%f %Z")
date1 = pd.to_datetime(d1, format = "%Y-%m-%d %H:%M:%S.%f %Z")



for x in range(len(d1)):
    #delta.append(date1[x] - date0[x])
    delta.append((date1[x] - date0[x]).total_seconds()/60.0)





    
plt.plot(date0,delta,'og')
plt.xticks(rotation=90)
plt.xlabel('Dates of 911 Calls')
plt.ylabel('Reaction Time of Operator to Dispatch a Unit (min)')
plt.title('Time Series Plot: Reaction Time of 911 Operator')
plt.axis(["2018-01-13","2018-01-25", 0 ,100])
plt.grid(True)
plt.show()

outlier(delta)


print("Average: " + str(average(delta)))
print("Standard Deviation: " + str(standard_deviation(delta)))









