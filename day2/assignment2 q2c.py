#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:28:28 2023

@author: dai
"""



##Assignment2 c

for i in range(7,-1,-2):
    for j in range((7-i)//2):
        print(" ",end="")
    for j in range(i):
        if j%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
