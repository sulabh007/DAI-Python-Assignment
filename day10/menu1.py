import sqlite3
from sqlite3 import Error


try:
    conn=sqlite3.connect("emp.db")
    print("Connected")
except Error as e:
    print(e)

def create_table():
    try:
        cursor=conn.cursor()
        table = """ CREATE TABLE IF NOT EXISTS EMPLOYEE (
                Eid INT NOT NULL,
                Ename TEXT NOT NULL,
                Mobile TEXT ,
                Salary INT,
                Department TEXT NOT NULL,
                Designation TEXT
            ); """
        cursor.execute(table)
        print("Table Created")
    except Error as e:
        print(e)

def addNewEmp(eid, ename, mobile, sal, dept, des):
    try:
        cursor.execute("insert into EMPLOYEE values(?,?,?,?,?,?);",(eid, ename, mobile, sal, dept, des))
        print("Added Successfully")
        conn.commit()   
    except Exception as e:
        print("error ocuured ",e)
        conn.rollback()

def delEmp(eid):
    try:
        cursor.execute("delete from Employee where eid=?;",(eid))
        conn.commit()
        print("Deleted Successfully")
    except Exception as e:
        print("error ocuured ",e)
        conn.rollback()
def ModifybyID(eid, ename, mobile, sal, dept, des):
    try:
        cursor.execute("update EMPLOYEE set Ename=?, Mobile=?, Salary=?, Department=?, Designation=? where Eid=?;",(ename, mobile, sal, dept, des,eid))
        print("Modified Successfully")
        conn.commit()   
    except Exception as e:
        print("error ocuured ",e)
        conn.rollback()

def displayAll():
    cursor.execute("select * from employee;")
    for row in cursor.fetchall():  #[(123,"xx",34,3456),(124,yyyy,56,7777)]
        print(f"""
              Eid: {row[0]} 
              Ename: {row[1]} 
              Mobile: {row[2]} 
              Salary: {row[3]}
              Department: {row[4]}
              Designation: {row[5]}
              """)
 
def displayByID(eid):
    try:
        cursor.execute(f"select * from employee where eid={eid};")
        row = cursor.fetchone()  #[(123,"xx",34,3456),(124,yyyy,56,7777)]
        print(f"""
              Eid: {row[0]} 
              Ename: {row[1]} 
              Mobile: {row[2]} 
              Salary: {row[3]}
              Department: {row[4]}
              Designation: {row[5]}
              """)
    except Exception as e:
        print("error occured",e)

def DisplayBasedonSal(sal):
    try:
        cursor.execute(f"select * from employee where salary>{sal};")
        for row in cursor.fetchall():  #[(123,"xx",34,3456),(124,yyyy,56,7777)]
            print(f"""
                  Eid: {row[0]} 
                  Ename: {row[1]} 
                  Mobile: {row[2]} 
                  Salary: {row[3]}
                  Department: {row[4]}
                  Designation: {row[5]}
                  """)
    except Exception as e:
        print("error occured",e)
