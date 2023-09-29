#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:42:45 2023

@author: dai
"""
lst=[5, 10, 15, 25, 50]
def addlst( pos=-1):
    inp=int(input("Enter a Number to be added"))
    cmd=str(input("Are you sure Y/N"))
    if pos is -1: 
        if cmd=="y"or "Y":
            lst.append(inp)
            return 1
        else:
            return 2
    else:
        if cmd=="y"or "Y":
            lst.insert(pos ,inp)
            return 1
        else:
            return 2

def removeByValue(ch):
    if lst.index(ch):
        cmd=str(input("Are you sure Y/N"))
        if cmd=="y"or "Y":
            lst.remove(ch)
            return 1
        else:
            return 2
       
    else:
        return 3

def removeByPos(ch):
    if ch<len(lst):
        cmd=str(input("Are you sure Y/N"))
        if cmd=="y"or "Y":
            lst.pop(ch)
            return 1
        else:
            return 2
       
    else:
        return 3

def sortLst(ch):
    global lst
    if ch == "a":
        cmd=str(input("Are you sure Y/N"))
        if cmd=="y"or "Y":
            
            lst.sort()
            return 1
        else:
            return 2
        
    elif ch == "b":
        cmd=str(input("Are you sure Y/N"))
        if cmd=="y"or "Y":
            
            lst.sort(reverse=True)
            return 1
        else:
            return 2
        
    else:
        return 3

def lstReverse():
    cmd=str(input("Are you sure Y/N"))
    if cmd=="y"or "Y":  
        lst.reverse()
        return 1
    else:
        return 2

def printLstSorted(rvs=False):
    lst1=[]
    lst1=lst.copy()
    lst1.sort(reverse=rvs)
    print(lst1)

def printLst(ch):
    if ch=="a":  
        list(map(lambda x:print(x,end=" "),lst))
    elif ch=="b":
        for x, y in enumerate(lst):
            print(x,y,sep=" ")
    