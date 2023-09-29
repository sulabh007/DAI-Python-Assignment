#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:03:31 2023

@author: dai
""" 
import numpy as np

sales= np.random.randint(10, size=(2,10,6))

print(sales)

for i in range(10):
    print("YearWise Sale of dealers of each item are:")
    print(f"""Year {i+1}
              Dealer1: {sales[0][i]}
              Dealer2: {sales[1][i]}""")
              
for i in range(10):
    print("Total YearWise Sale of dealers are:")
    print(f"""Year {i+1}
              Dealer1: {np.sum(sales[0][i])}
              Dealer2: {np.sum(sales[1][i])}""")
              
year=int(input("Enter a year of sales: "))

print(f"Sale of dealers of year {year} are:")
print(f"""Year {i+1}
          Dealer1: {sales[0][(year%2000)-1]}
          Dealer2: {sales[1][(year%2000)-1]}""")
          
for i in range(10):
    print("YearWise Sale of dealers of Tv and freeze are:")
    print(f"""Year {i+1}
              Dealer1: {sales[0][i][0]}  {sales[0][i][1]}
              Dealer2: {sales[1][i][0]}  {sales[1][i][1]}""")