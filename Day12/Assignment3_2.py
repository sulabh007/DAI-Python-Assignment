#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:26:25 2023

@author: dai
"""

import pandas as pd

data = [1,2,3,4,5], [ 5,2,2,4,6], [1,2,5,3,2], [ 1,4,3,2,1], [5,1,2,2,5]
idx=['2010','2011','2012','2013','2014']
col=['TV','Fridge','Mobile','Washing Machine', 'PC']
df= pd.DataFrame(data,index=idx,columns=col)



import matplotlib.pyplot as plt

s=df.max(axis=1)
plt.pie(s, labels=df.index, startangle=90)

df.plot(kind="area")


plt.show()


print("YearWise Pie chart")

y10=df.iloc[0]
plt.pie(y10, labels=col)
plt.title('2010')
plt.show()

y11=df.iloc[1]
plt.pie(y11, labels=col)
plt.title('2011')
plt.show()

y12=df.iloc[2]
plt.pie(y12, labels=col)
plt.title('2012')
plt.show()

y13=df.iloc[3]
plt.pie(y13, labels=col)
plt.title('2013')
plt.show()

y14=df.iloc[4]
plt.pie(y14, labels=col)
plt.title('2014')
plt.show()

