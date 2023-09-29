#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:33:41 2023

@author: dai
"""


##Assignment4

str1=str(input("enter a string1"))

lower=""
upper=""
for char in str1:
    if char.islower():
        lower=lower+char
    else:
        upper=upper+char

print(lower+upper)
