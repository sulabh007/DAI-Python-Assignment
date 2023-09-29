####Assignment1
##
##date= int(input("Enter the number days the months have: "))
##day= int(input("Enter the days the months Begins, 0 for monday and so on: "))
##
##d=1
##print("\tM\tTu\tW\tTh\tF\tSa\tSu")
##print("\t "*day, end=" ")
##for i in range(1, date+1):
##    print(f"\t{i}", end=" ")
##    if((day+i)%7==0):
##        print()


####Assignment2
##
##def histogram(lis):
##    for el in lis:
##        print("*"*el)
##
####lis=[4,9,7]
##lst = []
## 
##n = int(input("Enter number of elements : "))
## 
##for i in range(n):
##    ele = int(input())
##    lst.append(ele) 
##histogram(lst)
    
####Assingment3
##
##str1=str(input("Enter a Phrase: "))
##
##new_str="".join(ch for ch in str1 if ch.isalpha()).lower()
##
##rvs_str=new_str[::-1]
##
##if rvs_str==new_str:
##    print("It is a plaindrome")
##else:
##    print("It is not a plaindrome")

####Assignment4
##
##def pangram(str1):
##    new_str=str1.lower()
##    check="qwertyuiopasdfghjklzxcvbnm"
##    ans=False
##    for ch in check:
##        if(new_str.find(ch)==-1):
##            ans=False
##            break
##        ans=True
##    return ans;
##
##
##str1=str(input("Enter a Phrase: "))
##
##
##
##
##if (pangram(str1)):
##    print("It is a pangram")
##else:
##    print("It is not a pangram")

####Assignment 5
##
##def robberslang(str1):
##    check="AaEeIiOoUu "
##    ans=""
##    for ch in str1:
##        if (check.find(ch)==-1):
##            ans=ans+ch+"o"
##        ans=ans+ch
##    return ans
##
##str1=str(input("Enter a Phrase: "))
##print(robberslang(str1))

####Assignment 6
##
##def fact(n):
##    if n==1:
##        return 1;
##    return n*fact(n-1)
##
##for i in range(1,21):
##    print(i,fact(i),sep=" ")


####Assignment 7
##
##def Sum(n):
##    if n==0:
##        return 0
##    return n+Sum(n-1)
##
##num=int(input("Enter a number: "))
##print(Sum(num))


    


    
