#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:47:47 2023

@author: dai
"""

class Student:
    count=0
    
    def CGPAcal(self):
        return format(((self.__m1/3)+(self.__m2/2)+(self.__m3/4)), ".2f")  
    
    def __init__(self, sname='', m1=0, m2=0, m3=0):
        Student.count=Student.count+1
        self.__sid=Student.count
        self.__sname=sname.capitalize()
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3
        self.__CGPA=Student.CGPAcal(self)
    
    #setter method   
    def set_name(self,enm):
        self.__sname=enm
    def set_m1(self,m1):
        self.__m1=m1
    def set_m2(self,m2):
        self.__m2=m2
    def set_m3(self,m3):
        self.__m3=m3
    def set_CGPA(self):
        self.__CGPA=Student.CGPAcal(self)
        
    #getter method   
    def get_sid(self):
        return self.__sid
    
    def get_sname(self):
        return self.__sname
    
    def get_m1(self):
        return self.__m1
    
    def get_m2(self):
        return self.__m2
    
    def get_m3(self):
        return self.__m3
    
    def get_CGPA(self):
        return self.__CGPA
    
    def __str__(self):
        print("Student Details")
        print("------------------")
        str1=f"""
        StudentId: {self.__sid} 
        Name: {self.__sname} 
        Mark1:{self.__m1}
        Mark2:{self.__m2}  
        Mark3:{self.__m3}          
        """
        return str1
