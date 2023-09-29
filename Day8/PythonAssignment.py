import re

######################Assignment1#######################################
# line=str(input("Enter a Number: "))

# my_regex=r"^[987]\d{9}$"
    
# if re.match(my_regex,line, re.I|re.M): 
#     print(line)

######################Assignment2a#######################################

# with open("productdata.txt","r") as fh:
#     with open("myproduct.txt","w") as fh1:
#         for line in fh:
#             if re.match("^12.*0$",line):
#                 fh1.write(line)
    

######################Assignment2b#######################################

# dict1={}
# with open("productdata.txt","r") as fh:
#     for line in fh:
#         lst=line.strip("\n").split(":")
#         if dict1.get(lst[3]):
#             dict1[lst[3]]=dict1[lst[3]]+int(lst[4])
#         else:
#             dict1.setdefault(lst[3],int(lst[4]))
#         print(dict1)
######################Assignment2c#######################################

# with open("productdata.txt","r") as fh:
#     cat=str(input("Enter a category "))
#     cat=cat
#     for line in fh:
        
#         m=re.search(cat,line)
#         if m:
#             lst=line.split(":")
#             print(lst[1])