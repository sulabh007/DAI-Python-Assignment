from menu1 import *
if __name__=="__main__":
    cursor=conn.cursor()
    #print(cursor)
    create_table()
    choice=0
    
    while choice!=7:
        choice=int(input("""
                     1. Add new employee
                     2. Delete an employee
                     3. Modify an employee's details
                     4. Display all employees 
                     5. Display employee based on empid
                     6. Display all employee with sal > given sal
                     7. To exit 
                     Enter a choice: """))
        match choice:
            case 1:
                eid=input("Enter our id")
                ename=input("Enter a name: ")
                mobile=input("Enter a mobile number: ")
                sal= int(input("Enter the salary: "))
                dept=input("Enter the department: ")
                des=input("Enter the Designation: ")
                addNewEmp(eid, ename, mobile, sal, dept, des)
            case 2:
                eid=input("Enter our id")
                delEmp(eid)
            case 3:
                eid=input("Enter our id")
                ename=input("Enter a name: ")
                mobile=input("Enter a mobile number: ")
                sal= int(input("Enter the salary: "))
                dept=input("Enter the department: ")
                des=input("Enter the Designation: ")
                ModifybyID(eid, ename, mobile, sal, dept, des)
            case 4:
                displayAll()
            case 5:
                eid=input("Enter our id")
                displayByID(eid)
            case 6:
                sal= int(input("Enter the salary: "))
                DisplayBasedonSal(sal)
            case 7:
               print("Thank you for visiting....")
               conn.close()
            
    