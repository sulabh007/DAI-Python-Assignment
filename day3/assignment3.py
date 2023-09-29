##Assignment1
str1=str(input("enter a string"))
l= len(str1)

if l<7 and l%2==0:
    print("Invalid input")
else:
    idx=(l//2)-1
    print(str1[idx:idx+3])
