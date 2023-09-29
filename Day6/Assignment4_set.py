##############################Assignment1######################################

# sampleSet = {"Yellow", "Orange", "Black"}
# sampleList = ["Blue", "Green", "Red", "Yellow", "orange"]

# sampleSet.update(sampleList)
# print(sampleSet)

##############################Assignment2######################################

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# print(set1.intersection(set2))

##############################Assignment3######################################

# set1 = {10, 20, 30, 40, 50,25}
# set2 = {30, 40, 50, 60, 70,100}

# print(set1.symmetric_difference(set2))

##############################Assignment4######################################

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.union(set2))
# print(set1.symmetric_difference(set2))
# set1.difference_update(set2)
# set1.symmetric_difference_update(set2)
# print(set1)
# set1 = {10, 20, 30, 40, 50}
# print(set1)


##############################Assignment5######################################
# import functools
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# x=functools.reduce(lambda a, b: a+b, set1)
# avg=x/len(set1)

# x=set(filter(lambda x: x>avg, set2))

# set1.update(x)
# print(set1)

##############################Assignment6######################################
# st=set()
# # for i in range(0,1):
# #     lst.append([])
# n=int(input("Enter a Limit for element of set"))

# inp=str((input("Enter a element for set")))
# while inp!="":
#     if len(inp)>n:
#         st.add(inp)
#     inp=input("Enter a element for set/ Press Enter to quit")

# print(st)