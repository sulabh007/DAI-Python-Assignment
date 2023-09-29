#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:33:57 2023

@author: dai
"""


##Assignment5

str1=str(input("enter a string1"))
str2=str(input("enter a string2"))
ans=""
m=min(len(str1),len(str2))
for i in range(m):
    ans=ans+str1[i]+str2[0-1-i]
if len(str1)>m:
    ans=ans+str1[m:]
elif len(str2)>m:
    ans=ans+str2[0:len(str2)-m]
print(ans)

