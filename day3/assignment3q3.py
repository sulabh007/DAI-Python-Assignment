#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:33:09 2023

@author: dai
"""




##Assignment3

str1=str(input("enter a string1"))
str2=str(input("enter a string2"))

str3=str1[0]+str2[0]+str1[len(str1)//2]+str2[len(str2)//2]+str1[-1]+str2[-1]

print(str3)

