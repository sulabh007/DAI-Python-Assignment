###############################Assignment1.1################################
from student_class import 8   
    
# if __name__=="__main__": 
#     s=Student("Kishori",89,69,77)
#     print(s)

###############################Assignment1.2################################

# student_details={}


# def addnewStudent():
#     enm=input("Enter name ")
#     m1=int(input("Enter Marks 1 "))
#     m2=int(input("Enter Marks 2 "))
#     m3=int(input("Enter Marks 3 "))
#     st=Student(enm,m1,m2,m3)
#     student_details[st.get_sid()]=st

# def displayall():
#     for v in student_details.values():
#         print(v)
        
# def Searchpbyid(eid):
#     v=student_details.get(eid,-1)
#     return v

# def Searchpbyname(name):
#     for i,j in (student_details.items()):
#         if j.get_sname()==name:
#             return j
#     return -1

# def Get_StudentGPA(inp):
#     v=student_details.get(inp,-1)
#     if v!=-1:
#         return v.get_CGPA()
#     return -1
    
                
# if __name__=="__main__": 
#     # s=Student("Kishori",89,69,77)
#     # s1=Student("Kishor",89,69,69)
#     choice=0
#     while choice!=6:
        
#         choice=int(input("""
#             1. Add new Student
#             2. Display All Student
#             3. Search by id
#             4. Search by name
#             5. calculate GPA of a student
#             Enter Your Choice: """))
    
#         match choice:
#             case 1:
#                 addnewStudent()
#             case 2:
#                 displayall()
#             case 3:
#                 inp=int(input("Enter Student ID to Search : "))
#                 status=Searchpbyid(inp)
#                 if status==-1:
#                     print(f"No Student with id {inp} found")
#                 else:
#                     print(status)
        
#             case 4:
#                 inp=str(input("Enter Student Name to Search: "))
#                 inp=inp.capitalize()
#                 status=Searchpbyname(inp)
#                 if status==-1:
#                     print(f"No Student with name {inp} found")
#                 else:
#                     print(status)
            
#             case 5:
#                 inp=int(input("Enter Student id to Display its CGPA: "))
#                 status=Get_StudentGPA(inp)
#                 if status==-1:
#                     print(f"No Student with name {inp} found")
#                 else:
#                     print(status)
            
   
    
            
        
        
        