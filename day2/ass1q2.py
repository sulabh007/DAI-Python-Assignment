#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:21:35 2023

@author: dai
"""


##Assignment2

a=int(input("Enter a number"))
n2000=n500=n100=n50=n10=n5=n2=n1=0

if a>=2000:
    n2000=a//2000
    a=a%2000
if a>=500 and a<2000:
    n500=a//500
    a=a%500
if a>=100 and a<500:
    n100=a//100
    a=a%100
if a>=50 and a<100:
    n50=a//50
    a=a%50
if a>=10 and a<50:
    n10=a//10
    a=a%10
if a>=5 and a<10:
    n5=a//5
    a=a%5
if a>=2 and a<5:
    n2=a//2
    a=a%2
if a==1:
    n1=1

s=n2000+n500+n100+n50+n10+n5+n2+n1
print(s)
print(f"""
2000 note:{n2000}
500 note:{n500}
100 note:{n100}
50 note:{n50}
10 note:{n10}
5 coin:{n5}
2 coin:{n2}
1 coin;{n1}
""")
