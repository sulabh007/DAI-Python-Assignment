#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:33:12 2023

@author: dai
"""

import numpy as np

lists=[]

for i in range(20):
    element=int(input(f"Enter List{((i+1)//5)+1} Element {(i)%5}: "))
    lists.append(element)
    
list1=np.array(lists[:5])
list2=np.array(lists[5:10])
list3=np.array(lists[10:15])
list4=np.array(lists[15:20])

list_2d_1= np.array([list1, list2])
list_2d_2= np.array([list3, list4])

print("ADD:\n", list_2d_1+list_2d_2)
print("*"*20)
print("SUB:\n", list_2d_1-list_2d_2)
print("*"*20)
print("Multi:\n", list_2d_1*list_2d_2)
print("*"*20)
print("Division:\n", list_2d_1/list_2d_2)
print("*"*20)
print ("Expo array : ", np.exp(list_2d_1))