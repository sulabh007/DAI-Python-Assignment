#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:43:03 2023

@author: dai
"""

import sqlite3
from sqlite3 import Error



try:
    conn=sqlite3.connect("data.db")
    print("Connected")
except Error as e:
    print(e)

cursor=conn.cursor()

def create_table():
    try:
        cursor=conn.cursor()
        table = """ CREATE TABLE IF NOT EXISTS user(
                Uid INTEGER PRIMARY KEY AUTOINCREMENT,
                Uname TEXT NOT NULL,
                Address TEXT,
                Mobile TEXT ,
                Email TEXT NOT NULL
            ); """
        cursor.execute(table)
        print("Table Created")
    except Error as e:
        print(e)

def addNewUser(uname, add, mobile, email):
    try:
        cursor.execute("insert into user (uname, address, mobile, email) values(?,?,?,?);",( uname, add, mobile, email))
        print("Added Successfully")
        conn.commit()   
    except Exception as e:
        print("error ocuured ",e)
        conn.rollback()

def delEmp(uid):
    try:
        cursor.execute("delete from user where uid=?;",(uid))
        conn.commit()
        print("Deleted Successfully")
    except Exception as e:
        print("error ocuured ",e)
        conn.rollback()

def displayAll():
    cursor.execute("select * from user;")
    for row in cursor.fetchall():  #[(123,"xx",34,3456),(124,yyyy,56,7777)]
        print(f"""
              Uid: {row[0]} 
              Uname: {row[1]} 
              Address: {row[2]}
              Mobile: {row[3]} 
              Email: {row[4]}
              """)
 
def displayByName(ename, add):
    try:
        cursor.execute(f"select * from user where uname='{ename}' AND address='{add}';")
        row = cursor.fetchone()  #[(123,"xx",34,3456),(124,yyyy,56,7777)]
        print(f"""
              Uid: {row[0]} 
              Uname: {row[1]} 
              Address: {row[2]}
              Mobile: {row[3]} 
              Email: {row[4]}
              """)
        
            
    except Exception as e:
        mobile=input("Enter a mobile number: ")
        email=input("Enter the Email: ")
        addNewUser(ename, add, mobile, email)

if __name__=="__main__":
    cursor=conn.cursor()
    #print(cursor)
    create_table()
    choice=0
    
    while choice!=5:
        choice=int(input("""
                     1. Add new employee
                     2. Delete an employee
                     3. Display USER based on id
                     4. Display all
                     5. To exit 
                     Enter a choice: """))
        match choice:
            case 1:
                uname=input("Enter a name: ")
                mobile=input("Enter a mobile number: ")
                add= input("Enter the address: ")
                email=input("Enter the Email: ")
                addNewUser(uname, add, mobile, email)
            case 2:
                eid=input("Enter your id")
                delEmp(eid)
            case 3:
                ename=input("Enter your name: ")
                add=input("Enter Address: ")
                displayByName(ename, add)
            case 4:
                displayAll()
            case 5:
               print("Thank you for visiting....")
               conn.close()
            