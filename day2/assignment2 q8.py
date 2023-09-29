#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:30:50 2023

@author: dai
"""


##Assignment8


x= int(input("Enter number of a series: "))
n= int(input("Enter number of term: "))
s=x
t=x
print(x,end="")
for i in range(1,n):
    t=t+x*pow(10,i)
    s=s+t
    print("+",t,end="")

print("\nSum of Series:", s)
