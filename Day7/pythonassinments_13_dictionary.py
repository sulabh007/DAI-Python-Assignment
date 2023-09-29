##############################Assignment1###############################
# rot13={'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b',
# 'p':'c','q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R',
# 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F',
# 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

# def encode(str1):
#     ans=""
#     for i in str1:
#         if i.isalpha():
#             ans=ans+rot13[i]
#         else:
#             ans=ans+i
#     return ans
    
# sct="Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
# print(encode(sct))


##############################Assignment2###############################
# people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
# ch=int(input("""
# 1. Find out how many students are in the list
# 2. Change Lisa’s favourite colour
# 3. Remove 'Jenny' and her favourite colour
# 4. Sort and print students and their favourite colours alphabetically by name             
#     Enter Your choice: """))

# match ch:
#     case 1:
#         print(len(people))
#     case 2:
#         inp=str(input("Enter new color"))
#         people['Lisa']=inp
#     case 3:
#         people.pop("Jenny")
#     case 4:
#         people=sorted(people.items())
#         print(people)

##############################Assignment3###############################
# from menu_dict import *

# vdct={"0":{'name':'Vinod','vehicle':'Nano'},
#       "1":{'name':'Binod','vehicle':'Zen'},
#       "2":{'name':'Vishal','vehicle':'Swfit'}, 
#       "3":{'name':'Sam','vehicle':'Wangonr'}}



# choice=0
# choice=int(input("""
# 1. Add new person name and a vehicle name.
# 2. Delete a person name and vehicle name from the dictionary.
# 3. Modify vehicle name for the person
# 4. Search vehicle for the given person’s name.
# 5. Search list of people, who have given a vehicle
# 6. Display all person names.
# 7. Display all vehicle names.
# 8 Exit
# Enter your Choice: """))
# while choice!=8:
#     match choice:
#         case 1:
#             uname=str(input("Enter new name"))
#             vehicle=str(input("Enter vehicle name"))
#             uname=uname.capitalize()
#             vehicle=vehicle.capitalize()
#             status=addNewName(vdct, uname, vehicle)
#             if status==1:
#                 print("Added Successfully")
#             elif status==2:
#                 print("terminate the process")
#             else:
#                 print(f"{status['name']} already has {status['vehicle']}")
#         case 2:
#             uname=str(input("Enter name"))
#             uname=uname.capitalize()
#             status=DeleteName(vdct, uname)
#             if status==1:
#                 print("Deleted Successfully")
#             elif status==3:
#                 print("terminate the process")
#             else:
#                 print("User not found")
#         case 3:
#             uname=str(input("Enter  name"))
#             vehicle=str(input("Enter vehicle name"))
#             uname=uname.capitalize()
#             vehicle=vehicle.capitalize()
#             status=UpdateValue(vdct, uname, vehicle)
#             if status==1:
#                 print("Updated")
#             elif status==2:
#                 print("terminate the process")
#             else:
#                 print("No user found ")
#         case 4:
#             uname=str(input("Enter name"))
#             uname=uname.capitalize()
#             status=SearchByName(vdct, uname)
#             if status==1:
#                 print("Founded Successfully")
#             else:
#                 print("No user found")
#         case 5:
#             vehicle=str(input("Enter vehicle name"))
#             vehicle=vehicle.capitalize()
#             status=SearchByValue(vdct, vehicle)
#             if status==1:
#                 print("Founded Successfully")
#             else:
#                 print("No user found")
#         case 6:
#             status=disName(vdct)
            
#         case 7:
#             status=disValue(vdct)
#         case other:
#             print("Enter Valid Choice")
        
        

# ##############################Assignment4###############################
# from menu_dict import *

# vdct={"0":{'city':'Delhi','tree':['Neem','Tulsi']},
#       "1":{'city':'Patna','tree':['Ashoka']},
#       "2":{'city':'Nagpur','tree':['Tulsi']}, 
#       "3":{'city':'Pune','tree':['Neem']}}



# choice=0
# choice=int(input("""
# 1. Add new city and trees commonly found in the city.
# 2. Display all cities and the list of trees for all cities.
# 3. Display list of trees of a particular city.
# 4. Display cities which have the given tree.
# 5. Delete city
# 6. Modify tree list
# 7. Exit
# Enter your Choice: """))

# while choice!=7:
#     match choice:
#         case 1:
#             uname=str(input("Enter new city "))
#             tree=str(input("Enter trees name "))
#             uname=uname.capitalize()
#             tree=tree.capitalize()
#             trees=[]
#             while tree!='':
#                 trees.append(tree)
#                 tree=str(input("Enter trees name "))
#                 tree=tree.capitalize()
#             status=addNewName(vdct, uname, trees)
#             if status==1:
#                 print("Added Successfully")
#             elif status==2:
#                 print("terminate the process")
#             else:
#                 print(f"{status['city']} already has {status['tree']}")
#         case 2:
#             status=disAll(vdct)
#         case 3:
#             uname=str(input("Enter city "))
#             uname=uname.capitalize()
#             status=SearchByName(vdct, uname)
#             if status==1:
#                 print("Founded Successfully")
#             else:
#                 print("No user found")
#         case 4:
#             tree=str(input("Enter vehicle name "))
#             status=SearchByValue(vdct, tree)
#             if status==1:
#                 print("Founded Successfully")
#             else:
#                 print("No user found")     
#         case 5:
#             uname=str(input("Enter city "))
#             uname=uname.capitalize()
#             status=DeleteName(vdct, uname)
#             if status==1:
#                 print("Deleted Successfully")
#             elif status==2:
#                 print("terminate the process")
#             else:
#                 print("city not found")
#         case 6:
#             uname=str(input("Enter  name "))
#             uname=uname.capitalize()
#             choice=int(input("1. Add tree name\n2.Delete one Tree\n3.Modify Entirely\n"))
#             tree=str(input("Enter trees name "))
#             tree=tree.capitalize()
#             trees=[]
#             if choice==3 or choice==1:
#                 while tree!='':
#                     trees.append(tree)
#                     tree=str(input("Enter trees name "))
#                     tree=tree.capitalize()
#                 status=UpdateValue(vdct, uname, choice, trees)
#             else:
#                 status=UpdateValue(vdct, uname, choice, tree)
#             if status==1:
#                 print("Updated")
#             elif status==2:
#                 print("terminate the process")
#             else:
#                 print("No user found ")
#         case other:
#             print("Enter Valid Choice")
        

        