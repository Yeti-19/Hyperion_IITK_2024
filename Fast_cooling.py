import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as sci

### CASE 1 ###

df=pd.read_csv('fast_cooling.csv')
df2=df[df['Frequency']<1.0e+14]

def func(a,b):
    return a*(df2['Frequency'])**b

ydata=df2['Fv_fast_cooling']
xdata=df2['Frequency']
x0=[1,3]

fig = plt.figure("Case 1")

a=sci.curve_fit(func,xdata,ydata)[1][0]
b=sci.curve_fit(func,xdata,ydata)[0][0]

plt.xlabel('Frequency', fontsize = 18)
plt.ylabel('Fv_fast_cooling', fontsize = 18)

plt.scatter(xdata,ydata)
plt.show()


### CASE 2 ###

df=pd.read_csv('fast_cooling.csv')

df2=df[df['Frequency']>1.0e+14]
df2=df2[df2['Frequency']<1.0e+16]

def func(a,b):
    return a*(df2['Frequency'])**b

ydata=df2['Fv_fast_cooling']
xdata=df2['Frequency']
x0=[1,3]

fig = plt.figure("Case 2")

a=sci.curve_fit(func,xdata,ydata)[1][0]
b=sci.curve_fit(func,xdata,ydata)[0][0]

plt.xlabel('Frequency', fontsize = 18)
plt.ylabel('Fv_fast_cooling', fontsize = 18)

plt.scatter(xdata,ydata)
plt.show()

