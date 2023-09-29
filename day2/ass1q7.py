#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:23:21 2023

@author: dai
"""

##Assignment7
x=int(input("Enter unit"))
a=0
if x>200:
    a=a+((x-200)*10)
    x=200
if x>100 and x<=200:
    a=a+((x-100)*5)

print(a)
