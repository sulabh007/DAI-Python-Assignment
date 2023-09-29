##########################Assignment1##################################
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dict1={}

# for x,y in zip(keys, values):
#     dict1[x]=y
# print(dict1)

##########################Assignment2##################################

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = {**dict1, **dict2}
# print(dict3)

##########################Assignment3##################################


# sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
# print(sampleDict["class"]["student"]["marks"]["history"])

##########################Assignment4##################################
# sampleDict = {
# "name": "Kelly",
# "age":25,
# "salary": 8000,
# "city": "New york"
# }

# sampleDict.pop("name")
# sampleDict.pop("salary")
# print(sampleDict)

##########################Assignment5##################################

# sampleDict = {'a': 100, 'b': 200, 'c': 300,'d':200}

# # sampleDict = list(filter(lambda item: item[1]!=200, sampleDict.items()))

# values={}
# for key, value in sampleDict.items():
#     if value!=200:
#         values[key]=value
        
# print(values)

##########################Assignment6##################################

# sampleDict = {
# "name": "Kelly",
# "age":25,
# "salary": 8000,
# "city": "New york"
# }

# value=sampleDict['city']
# sampleDict.pop('city')
# sampleDict['location']=value

# print(sampleDict)

##########################Assignment7##################################
# sampleDict = {
# 'Physics': 82,
# 'Math': 65,
# 'history': 75}

# maxk=""
# maxv=0
# for key, value in sampleDict.items():
#     if maxv<value:
#         maxk=key
#         maxv=value
# print(maxk)

##########################Assignment8##################################
# sampleDict = {
# 'emp1': {'name': 'Jhon', 'salary': 7500},
# 'emp2': {'name': 'Emma', 'salary': 8000},
# 'emp3': {'name': 'Brad', 'salary': 6500}
# }

# inp= str(input("Enter the name: "))
# inp =inp.capitalize()

# for key, value in sampleDict.items():
   
#     if value['name']==inp:
        
#         sal=int(input("Enter new salary "))
       
#         if sal<value['salary']:
#             print("unable to modified")
#         else:
#             sampleDict[str(key)]['salary']=sal
#         break
# else:
#     print("Name not found")
        

