#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:31:49 2023

@author: dai
"""


##Assignment2

str1=str(input("enter a string1"))
str2=str(input("enter a string2"))



print(str1[0:(len(str1)//2)]+str2+str1[(len(str1)//2):])