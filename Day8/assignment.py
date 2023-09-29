##########################Assignment1####################################
import re
# email=str(input("Enter an Email "))

# my_regex="(\w+)@"

# m=re.match(my_regex, email, re.I|re.M)
# print(m.group().strip("@"))


##########################Assignment2####################################

# line=str(input("Enter a Line: "))

# while line!="":
#     my_regex=r"^\d{1}\D|^((\w)\2)(?!\2)"
    
#     if re.match(my_regex,line, re.I|re.M): 
#         print(line)
#     line=str(input("Enter a Line: "))


##########################Assignment3####################################
# line=str(input("Enter a Number: "))


# my_regex=r"^[987]\d{9}$"
    
# if re.match(my_regex,line, re.I|re.M): 
#     print(line)

##########################Assignment4####################################
# user=str(input("Enter a Username: "))

# user_reg="^[\w\d]+$"
# psw_reg=r"((\w+).*[\D\W].*(\d+).*)"
# attempts=3
# if re.match(user_reg,user): 
#     while attempts>0:
#         psw=str(input("Enter a Password: "))
#         if len(psw)<8:
#             print("password is too short")
#             print(f"Attempt Remaining: {attempts-1}")
#             continue
#         else:
#             if re.fullmatch(psw_reg,psw):
#                 print("welcome to our application.")
#                 break
#             else:
#                 print("Invalid Password, add special characters and number")
#                 print(f"Attempt Remaining: {attempts-1}")
#         attempts=attempts-1
# else:
#     print("Invalid User Name")
