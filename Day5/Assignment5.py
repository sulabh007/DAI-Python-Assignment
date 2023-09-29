####Assignment1
##
##aLsit = [100, 200, 300, 400, 500]
##aLsit.reverse()
##print(aLsit)


####Assignment2
##
##list1 = ["M", "na", "i", "Raj"]
##list2 = ["y", "me", "s", "esh"]
##
##lst=[]
##
##lst=list(map(lambda x,y:x+y,list1,list2))
##
##print(lst)

####Assignment3
##
##list1 = [1, 2, 3, 4, 5, 6, 7]
##
##
##lst=[]
##
##lst=list(map(lambda x:x*x,list1))
##
##print(lst)


##Assignment 4

def combine(list1, list2):
    ls=[]
    for ch in list1:
        for ch2 in list2:
            ls.append(ch+ch2)
    return ls

list1 = ["Hello ", "Welcome "]
list2 = ["Students", "Sir"]


print(combine(list1, list2))

####Assignment 5
##
##list1 = [10, 20, 30, 40]
##list2 = [100, 200, 300, 400]
##
##list(map(lambda x,y:print(x,y,sep=" "),list1, list(reversed(list2))))


####Assignment 6
##
##list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
##
##list1=list(filter(lambda x: x!="",list1))
##print(list1)


####Assignment 7
##
##list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
##
##list1[2][2].append(7000)
##print(list1)


####Assignment 8
##list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
##
##list2=["h", "i", "j"]
##
##list1[2][1][2].extend(list2)
##print(list1)



###Assignment 9
##
##list1 = [5, 10, 15, 20, 25, 50, 20]
##
##if list1.index(20):
##    list1[list1.index(20)]=200
##    
##print(list1)
##
####Assignment10
##list1 = [5, 10, 15, 20, 25, 50, 20]
##list1=list(filter(lambda x: x!=20,list1))
##print(list1)
