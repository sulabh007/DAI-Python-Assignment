#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 18:09:44 2023

@author: dai
"""

import re 

def addAge(row):
    return str(row['age'])+":"+row['views']

def replaceStr(str1):
    if re.match('[a-zA-Z]', str1):
        return '0'
    else:
        return str1
    

import pandas as pd
mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
#print(mymoviedata.head())
df=pd.DataFrame(mymoviedata)
df.columns=["sr.no", "age", "gender", "profession", "views"]
gender=df['gender']
#print(gender)
df['col6']= df.apply(addAge, axis=1)

df['views']= pd.to_numeric(df['views'].apply(replaceStr))

group= df.groupby(by="age").mean()



import matplotlib.pyplot as plt

group.plot(kind='bar', y='views')
plt.xlabel('age')
plt.show()


