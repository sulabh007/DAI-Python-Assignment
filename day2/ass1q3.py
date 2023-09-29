#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:22:04 2023

@author: dai
"""


##Assignment3

x=int(input("Enter a number of class"))
y=int(input("Enter a number of class attended"))

a=y/x*100
if(a<75):
    choice=input("Do you have a medical reason Y/N")
    if choice=="y":
        print("Provide report")
    else:
        print("Ineligible for exam")
else:
    print("eligible for exam")



