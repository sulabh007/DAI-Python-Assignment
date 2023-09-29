ammount = int(input("Enter the ammount: "))

if ammount>=2000:
    ans=ammount//2000
    print(f"you required {ans} notes of 2000")
    ammount=ammount-(ans*2000)
if ammount>=500:
    ans=ammount//500
    print(f"you required {ans} notes of 500")
    ammount=ammount-(ans*500)
if ammount>=200:
    ans=ammount//200
    print(f"you required {ans} notes of 200")
    ammount=ammount-(ans*200)
if ammount>=100:
    ans=ammount//100
    print(f"you required {ans} notes of 100")
    ammount=ammount-(ans*100)
if ammount>=50:
    ans=ammount//50
    print(f"you required {ans} notes of 50")
    ammount=ammount-(ans*50)
if ammount>=20:
    ans=ammount//20
    print(f"you required {ans} notes of 20")
    ammount=ammount-(ans*20)
if ammount>=10:
    ans=ammount//10
    print(f"you required {ans} notes of 10")
    ammount=ammount-(ans*10)
if ammount>=5:
    ans=ammount//5
    print(f"you required {ans} notes of 5")
    ammount=ammount-(ans*5)
if ammount>=2:
    ans=ammount//2
    print(f"you required {ans} coins of 2")
    ammount=ammount-(ans*2)
if ammount>=1:
    ans=ammount//1
    print(f"you required {ans} coins of 1")
    ammount=ammount-(ans*1)
else:
    print("You have entered wrong note")
