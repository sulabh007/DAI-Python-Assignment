#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:29:47 2023

@author: dai
"""


##Assignment5

no= int(input("Enter number: "))
s=0
while no!=0:
  d=no%10
  s=s+d
  no=no//10
print("Sum of digit is: ", s)
