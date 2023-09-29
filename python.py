'''import sys
def addition(n1,n2):
    return n1+n2
def factorial(n1):
    f=1
    for i in range(2,n1+1):
        f=f*i
    return f

choice=0
while choice!=3:
    choice=int(input("""
    1. Addition
    2. Factorial
    3. exit
    choice: """))
    if choice==1:
        n1=int(input("Enter number 1: "))
        n2=int(input("Enter number 2: "))
        s=addition(n1,n2)
        print(f"Addition: {s}")
    elif choice==2:
        n1=int(input("Enter a number: "))
        ans=factorial(n1)
        print(f"Factorial: {ans}")
    elif choice==3:
        print("Thank you for visiting...")
        sys.exit(0)
    else:
        print("wrong choice")'''



n1 = int(input("enter number classes held "))
n2 = int(input("number of classs atended "))
per=(n2/n1)*100
if per>=75:
    print("student is allowed")
else:
    print("student are not allowed")

    
