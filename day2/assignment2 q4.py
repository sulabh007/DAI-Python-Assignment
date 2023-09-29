#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:29:33 2023

@author: dai
"""


##Assignment4
s=0
choice="n"
c=0
while choice!="q":
    no= int(input("Enter number: "))
    choice= input("Press q to quit, n to continue")
    s=s+no
    c=c+1

avg= s/c
print(f"Sum is {s} and Average is {avg}")
