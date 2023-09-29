####################################Assignment1#################################
##
##
##
##print("""
##a. display characters from even position
##b. display characters from odd position
##c. display length of a string
##d. add a at the end of string length times
##e. exit
##""")
##
##choice=""
##while(choice!="e"):
##    choice= str(input("Enter your choice: "))
##    if(choice=="e"):
##        print("Program ended")
##        break
##    str1= str(input("Enter a String: "))
##    if choice=="a":
##        print(str1[::2])
##    elif choice=="b":
##        print(str1[1::2])
##    elif choice=="c":
##        print(len(str1))
##    elif choice=="d":
##        print(str1+("a"*len(str1)))
            


###############################Assignment2#####################################
##
##str1=str(input("Enter a String :"))
##str2=str(input("Enter a String to find "))
##pos=str1.find(str2)
##cnt=0
##while pos!=-1:
##    print(f"{str2} - {pos}")
##    pos=str1.find(str2,pos+1)
##    cnt=cnt+1
##print("Count :",cnt)



###############################Assignment3#####################################
# from menu_list import *

# print("""
# 1. Accept Data    
# 2. Delete data by value
# 3. delete data by position
# 4. sort
# 5. reverse
# 6. Print in sorted order without changing original list
# 7. print in reverse order without changing original list
# 8. display data

# """)

# choice= int(input("Enter your choice"))

# match choice:
#     case 1:
#         ch=str(input("a)add at last position\nb)add at given position "))
#         match ch:
#             case "a":
#                 status=addlst()
#                 if status==1:
#                     print("Succesfully added")
#                 else:
#                     print("Unable to add")
#             case "b":
#                 inp=int(input("Enter a Postion where number has to be added"))
#                 status=addlst(inp)
#                 if status==1:
#                     print("Succesfully added")
#                 else:
#                     print("Unable to add")
#             case other:
#                 print("enter valid choice")
#     case 2:
#         ch=int(input("Enter Value to be removed"))
#         status=removeByValue(ch)
#         if status==1:
#             print("Succesfully added")
#         elif status==2:
#             print("Founded element by not deleted")
#         else:
#             print("Not founded")
#     case 3:
#         ch=int(input("Enter position yo be removed"))
#         status=removeByPos(ch)
#         if status==1:
#             print("Succesfully added")
#         elif status==2:
#             print("Founded element by not deleted")
#         else:
#             print("Not founded")
#     case 4:
#         ch=str(input("a)Accesnding\nb)Descending\n"))
#         status=sortLst(ch)
#         if status==1:
#             print("Succesfully")
#         elif status==2:
#             print("Unable to sort")
#         else:
#             print("invalid choice")
#     case 5:
#         status=lstReverse()
#         if status==1:
#             print("Succesfully reversed")
#         else:
#             print("Unable to reverse")
#     case 6:
#         printLstSorted()
#     case 7:
#         printLstSorted(True)
#     case 8:
#         ch=str(input("a)Normal\nb)Numbered\n"))
#         printLst(ch)


###############################Assignment4#####################################

# n= int(input("enter size of list"))
# lst1=[]
# lst2=[]
# for i in range(n):
#     city= str(input(f"Enter name of {i+1}th city "))
#     loc= str(input(f"Enter name of {i+1}th location "))
#     lst1.append(city)
#     lst2.append(loc)

# for i,j in zip(lst1, lst2):
#     print(i,j, sep=" ")

###############################Assignment5#####################################
# lst=[12, 1, 3, 7, 8, 5, 8]

# ans=[-1]*(max(lst)+1)

# for i in range(len(lst)):
#     ans[lst[i]]=i

# print(ans)

###############################Assignment6#####################################
# from menu_set import *

# choice=0

# while choice!=8:
#     choice=int(input("""
# 1. delete element if exists otherwise do not show any errr
# 2. add a elemet   
# 3. create one more set
# 4. union of 2 sets             
# 5. intersection of 2 sets
# 6. difference of 2 sets
# 7. convert set into frozenset
# 8. exit
# Enter Your Choice """))

#     match choice:
#         case 1:
#             status=removeByValue()
#             if status==1:
#                 print("Successfully Deleted")
#             else:
#                 print("Unable to delete")
#         case 2:
#             status=addset()
#             if status==1:
#                 print("Successfully Deleted")
#             else:
#                 print("Unable to delete")
#         case 3:
#             status=CreateSet()
#             if status==1:
#                 print("Successfully created")
#             else:
#                 print("Unable to Create")
#         case 4:
#             status=UnionSet(st,st2)
#             if status==1:
#                 print("Successful")
#             elif status==3:
#                 print("Empty set found, create a set")
#             else:
#                 print("Unable to Print Union")
#         case 5:
#             status=InterSet(st,st2)
#             if status==1:
#                 print("Successful")
#             elif status==3:
#                 print("Empty set found, create a set")
#             else:
#                 print("Unable to Print Intersection")
#         case 6:
#             status=InterSet(st,st2)
#             if status==1:
#                 print("Successful")
#             elif status==3:
#                 print("Empty set found, create a set")
#             else:
#                 print("Unable to Print Difference")
#         case 7:
#             status=FrozenSet()
#             if status==1:
#                 print("Successfully frozen")
#             else:
#                 print("Unable to freeze")
#         case other:
#             print("Select valid option")
    
###############################Assignment7#####################################

# lst=[]
# # for i in range(0,1):
# #     lst.append([])

# inp=input("Enter a Number")
# while inp.isdigit():
#     inp=int(inp)
#     r=(inp%10)
#     for i in range(len(lst),r+1): 
#         lst.append([])
    
#     lst[r].append(inp)
#     inp=input("Enter a Number/ Press any Letter to quit")

# print(lst)

###############################Assignment8#####################################

# lst= ["dxz","axz","bat","rat","bbc","bbm"]

# str1=str(input("Enter a String with length 3 EX: pat: "))

# if(len(str1)<2):
#     print("invalid input")

# index = [idx for idx, s in enumerate(lst) if str1[1:]==s[1:]]

# if index==[]:
#     lst.append(str1)
# else:
#     lst.insert(index[-1]+1, str1)

# print(lst)
