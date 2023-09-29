



##Assignment10
x=int(input("Enter cost of bike"))
if x>=100000:
    print(f"Tax is {x*15/100} Inssurance is {x*20/100} Total cost is {x+(x*35/100)}")
elif x>=50000 and x<100000:
    print(f"Tax is {x*10/100} Inssurance is {x*8/100} Total cost is {x+(x*18/100)}")
else:
    print(f"Tax is {x*5/100} Inssurance is {x*5/100} Total cost is {x+(x*10/100)}")

