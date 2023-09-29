##s1="this is a cat, cat is cute, where is your cat? mine is here"
##cat="cat"
##pos=s1.find(cat)
##while pos!=-1:
##    print(pos)
##    pos=s1.find(cat,pos+1)
##print("number of occurances :",s1.count(cat))
##
##print("*"*69)
##
##pos=s1.rfind(cat)
##while(pos!=-1):
##    print(pos)
##    pos= s1.rfind(cat,0,pos)
##print("number of occurances :",s1.count(cat))
##print(s1.replace("cat","dog"))
##
##
##s1="this is, test"
##print("uppercase ",s1.upper())
##print("lowercase ",s1.lower())
##print("startswith",s1.startswith("thi"))
##print("endswith",s1.endswith("thi"))
##print("split",s1.split(" "))
##print("split",s1.split(","))
##s2="asdaaaaddd this is test xxdddsssa"
##print("strip",s2.strip("sdx "))
##account="xxxxx3456xxxx"
##print("strip",account.strip("x"))
##lst=["aaa","ccc","vvvv"]
##print(":".join(lst))
##print("".join(lst))
##print("1234".isdecimal())
##print("lsdf".isalpha())
##print("this is new is this".replace("is", "xxxxxxxx"))
##print("this is new is this".replace("is", "xxxxxxxx",2))


##a=12
##b=a
##c=12
##print(id(a), id(b),id(c))
##d=int(input("enter number "))
##print(id(d))
##a=10
##print(id(a),id(b),id(c))
##print(a is b)
##s="Hello"
##t=s
##x="Hello"
##y=input("enter string ")
##print(id(s),id(t),id(x),id(y))

lst=[1,2,3,4,5,6]
lst1=["python","perl","test"]
lst2=[12,12,34,12,"xxx","bbb",34,56,[34,56,23],56]
print(lst2[8][1])
print(lst[3])
#To find length of the string
print("length",len(lst))
#to replace value at 3 rd index position
lst[3]=45
print(lst)

for i in lst1:
    print(i)

st="this is data"
for a in st:
    print(a,end="")

lst=[]
for i in range(2):
    num=int(input("\nenter number "))
    lst.append(num)
print(lst)

lst.extend(lst1)
print(lst)




lst.insert(4,12)
print(lst)
