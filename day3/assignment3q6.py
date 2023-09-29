#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:34:07 2023

@author: dai
"""


##Assignment6
str1=str(input("enter a string1"))

str1=str1.lower()

pos=0
while(pos!=-1):
    pos=str1.find("usa",pos+1)
    print(pos)
