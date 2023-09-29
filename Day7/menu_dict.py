

def values(value):
    x,y=value.items()
    x=x[1]
    if len(y[1:])==1:
        return (x,y[1])
    else:
        return (x,y[1:])

def addNewName(dct, uname, *val):
    for key, value in dct.items():
        y=list(value.keys())
        if value[y[0]]==uname:
            
            return value
        s=int(key)
    cmd=str(input("Are you sure Y/N"))
    if cmd=="y"or "Y":
        dct.setdefault(str(s+1), {y[0]:uname,y[1]:val})
        return 1
    else:
        return 2

def DeleteName(dct, uname):
    global vdct
    for key, value in dct.items():
        y=list(value.keys())
        if value[y[0]]==uname:
            x,y=values(value)
            print(f"Delete {x} with {y}")
            cmd=str(input("Are you sure Y/N"))
            if cmd=="y"or "Y":
                dct.pop(key)
                return 1
            else:
                return 2
        else:
            return 3
            
def UpdateValue(dct, uname, choice=3, *val):
    for key, value in dct.items():
        a=list(value.keys())
        if value[a[0]]==uname:
            x,y=values(value)
            print(f"Update {y} of {x}")
            cmd=str(input("Are you sure Y/N"))
            if cmd=="y"or "Y":
                if choice==3:
                    dct[key][a[1]]=val
                    return 1
                elif choice==2:
                    dct[key][a[1]].remove(val[0])
                    return 1
                elif choice==1:
                    dct[key][a[1]].extend(*val)
                    return 1
                else:
                    return 3
            else:
                return 2
    else:
        return 3
            
def SearchByName(dct, uname):
    for key, value in dct.items():
        y=list(value.keys())
        if value[y[0]]==uname:
            x,y=values(value)
            print(f"{x} has {y}")
            return 1
    else:
        return 2

def SearchByValue(dct, val):
    b=2
    for key, value in dct.items():
        y=list(value.keys())
        if val in value[y[1]]:
            x,y=values(value)
            print(f"{x} has {y}")
            b=1
    return b

def disName(dct):
    for key, value in dct.items():
        y=list(value.keys())
        print(value[y[0]])
    else:
        return 2
    return 1

def disValue(dct):
    for key, value in dct.items():
        y=list(value.keys())
        print(value[y[1]])
    return 1

def disAll(dct):
    for key, value in dct.items():
        y=list(value.keys())
        print(f"{y[0]}----->{value[y[0]]}")
        print(f"\t{y[1]}----->{value[y[1]]}")
        