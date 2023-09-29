#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:54:32 2023

@author: dai
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("weather_by_cities.csv")
print(df)

new_df=df.fillna(method="bfill")

city = new_df["city"]
temp = new_df["temperature"]

g= new_df.groupby("city")
g= new_df.groupby("city")


y=g['temperature'].max()

cities= y.index
temp=y.values

color=['r','b','g']

plt.pie(temp, labels=cities, colors=color, explode=(0,0.2,0), startangle=90)

# plt.bar(cities, temp)
# plt.xlabel("cities")
# plt.ylabel("max temperture")
# plt.title("temperature graph")
# plt.show()