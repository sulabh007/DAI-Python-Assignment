#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:31:02 2023

@author: dai
"""


##Assignment9
import math

x= int(input("Enter value of x: "))
n= int(input("Enter number of term: "))

s=0
for i in range(n):
  s=s+(1*pow(x,i))/math.factorial(i)
print("The sum is :",s)
