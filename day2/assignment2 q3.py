#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:29:11 2023

@author: dai
"""


##Assignment3

def gcd(a,b):
    while (a>0 and b>0):
        if a>b:
            a=a%b
        else:
            b=b%a
    if(a==0):
        return b
    return a

a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
print("GCD is ",gcd(a,b))
