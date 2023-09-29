#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:20:40 2023

@author: dai
"""

##Assignment1

x=int(input("Enter a number of class"))
y=int(input("Enter a number of class attended"))

a=y/x*100
if(a<75):
    print("Ineligible for exam")
else:
    print("eligible for exam")