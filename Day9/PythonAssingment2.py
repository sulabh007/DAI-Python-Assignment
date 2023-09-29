#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:06:42 2023

@author: dai
"""


class Friend:
    count=0
    
    
    def __init__(self, name='', lname='', hobbies=[], no=0, bday="XX-XX", add=""):
        Friend.count=Friend.count+1
        self.__id=Friend.count
        self.__name=name.capitalize()
        self.__lname=lname.capitalize()
        self.__hobby=hobbies
        self.__no=no
        self.__bday=bday
        self.__add=add
    
    
    #setter method   
    def set_name(self,enm):
        self.__name=enm
    def set_lname(self,lname):
        self.__lname=lname
    def set_hobby(self,hobby):
        self.__hobby=hobby
    def set_no(self,no):
        self.__no=no
    def set_bday(self):
        self.__bday=Student.bday(self)
    def set_add(self,add):
        self.__add=add
        
    #getter method   
    def get_sid(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_no(self):
        return self.__no
    
    def get_hobby(self):
        return self.__hobby
    
    def get_lname(self):
        return self.__lname
    
    def get_bday(self):
        return self.__bday
    
    def get_add(self):
        return self.__add
    
    def __str__(self):
        print("Friend Details")
        print("------------------")
        str1=f"""
        FriendId: {self.__id} 
        Name: {self.__name} 
        Last Name:{self.__lname}
        No:{self.__no}  
        Bday:{self.__bday}
        Hobbies:{self.__hobby} 
        Address:{self.__add}             
        """
        return str1
 

friends_details={}


def addnewFriend():
    hob=[]
    enm=input("Enter name ")
    lnm=input("Enter last name ")
    no=int(input("Enter no "))
    add=(input("Enter address "))
    bday=(input("Enter Birthday in DD-MM format "))
    hobby=(input("Enter hobbies "))
    while hobby!="":
        hob.append(hobby)
        hobby=(input("Enter hobbies "))
        
    fr=Friend(enm,lnm, hob, no, bday, add)
    friends_details[fr.get_sid()]=fr

def displayall():
    for v in friends_details.values():
        print(v)
        
def Searchpbyid(eid):
    v=friends_details.get(eid,-1)
    return v

def Searchpbyname(name):
    for i,j in (friends_details.items()):
        if j.get_name()==name:
            return j
    return -1

def Get_Friends_by_Hobby(inp):
    b=1
    for i,j in friends_details.items():
        lst=j.get_hobby()
        if inp in lst:
            print(j)
        else:
            b=-1
        
    return b        
       
if __name__=="__main__": 
    s=Friend("Kishori","panday",['reading','running'],9578412345,'01-01')
    t=Friend("Kishor","panday",['running'],9578512345,'11-01')
    
    choice=0
    while choice!=6:
        choice=int(input("""
        1. Display All Friends
        2. Search by id
        3. Search by name
        4. Display all friend with a particular hobby
        5. Add new Friend
        Enter Your Choice: """))
    
        match choice:
            case 1:
                displayall()
            case 2:
                inp=int(input("Enter Friends ID to Search : "))
                status=Searchpbyid(inp)
                if status==1:
                    print("Successful")
                else:
                    print(f"No Friends with id {inp} found")
        
            case 3:
                inp=str(input("Enter Friends Name to Search: "))
                inp=inp.capitalize()
                status=Searchpbyname(inp)
                if status==1:
                    print("Successful")
                else:
                    print(f"No Friends with name {inp} found")
            
            case 4:
                inp=str(input("Enter hobby to Search: "))
                status=Get_Friends_by_Hobby(inp)
                if status==1:
                    print("Successful")
                else:
                    print(f"No Friends with name {inp} found")
            
            case 5:
                addnewFriend()
        
