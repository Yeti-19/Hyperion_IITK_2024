import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as sci

df=pd.read_csv('HYPERION IITK/slow_cooling.csv')

# Run each case separately 

### CASE 1 ###

df2=df[df['Frequency']<1.0e+10]          # Condition for Case 1
def func(a,b):
    return a*(df2['Frequency'])**b       # Equation

fig = plt.figure("Case 1")

ydata=df2['Fv_slow_cooling']
xdata=df2['Frequency']
x0=[1,3]

a=sci.curve_fit(func,xdata,ydata)[1][0]
b=sci.curve_fit(func,xdata,ydata)[0][0]

plt.xlabel('Frequency', fontsize = 18)
plt.ylabel('Fv_slow_cooling', fontsize = 18)

plt.scatter(xdata,ydata)
plt.show()

### CASE 2 ###

df2=df[df['Frequency']>1.0e+10]
df2=df2[df2['Frequency']<1.0e+16]        # Condition for Case 2
def func(a,b):
    return a*(df2['Frequency'])**b       # Equation

fig = plt.figure("Case 2")

ydata=df2['Fv_slow_cooling']
xdata=df2['Frequency']
x0=[1,3]

a=sci.curve_fit(func,xdata,ydata)[1][0]
b=sci.curve_fit(func,xdata,ydata)[0][0]

plt.xlabel('Frequency', fontsize = 18)
plt.ylabel('Fv_slow_cooling', fontsize = 18)

plt.scatter(xdata,ydata)
plt.show()

### CASE 3 ###

df2=df[df['Frequency']>1.0e+16]          # Condition for Case 3

def func(a,b):
    return a*(df2['Frequency'])**b       # Equation

fig = plt.figure("Case 3")

ydata=df2['Fv_slow_cooling']
xdata=df2['Frequency']
x0=[1,3]

a=sci.curve_fit(func,xdata,ydata)[1][0]
b=sci.curve_fit(func,xdata,ydata)[0][0]

plt.xlabel('Frequency', fontsize = 18)
plt.ylabel('Fv_slow_cooling', fontsize = 18)

plt.scatter(xdata,ydata)
plt.show()






