#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:24:05 2023

@author: dai
"""

##Assignment9
x=int(input("Enter a Year"))
if (x)%400==0:
    print("Leap Year")
elif x%4==0 and x%100!=0:
    print("Leap year")
else:
    print("Nope")