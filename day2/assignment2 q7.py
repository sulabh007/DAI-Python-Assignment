#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:30:31 2023

@author: dai
"""


##Assignment7
s=0
for i in range(20):
    no= int(input(f"Enter number{i+1}: "))
    if no%2==0:
        s=s+no
print("The sum of even number", s)
