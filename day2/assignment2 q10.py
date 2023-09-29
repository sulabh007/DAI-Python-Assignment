#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:31:16 2023

@author: dai
"""


##Assignment10
x= int(input("Enter value of x: "))
n= int(input("Enter number of term: "))

s=0
for i in range(0,n):
  a=(pow(-1,i)*pow(x,2*i+1))
  s=s+a
  print(a)
print("The sum is :",s)

