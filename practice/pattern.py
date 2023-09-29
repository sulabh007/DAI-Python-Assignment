for i in range(6):
    for j in range(i):
        print("a", end="")
    for j in range(10-2*i):
        print(" ", end="")
    for j in range(i):
        print("a", end="")
    print()
for i in range(6):
    for j in range(5-i):
        print("a", end="")
    for j in range(2*i):
        print(" ", end="")
    for j in range(5-i):
        print("a", end="")
    print()
