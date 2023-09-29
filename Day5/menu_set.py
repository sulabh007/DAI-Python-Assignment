st={1,2,3,5,60,8,46,75,79,54,6,52,13,9}
st2=set()

def removeByValue():
    ch=int(input("Enter value to be deleted"))
    cmd=str(input("Are you sure Y/N"))
    if cmd=="y"or "Y":
        st.discard(ch)
        return 1
    else:
        return 2
       
def addset():
    inp=int(input("Enter a Number to be added"))
    cmd=str(input("Are you sure Y/N"))
    if cmd=="y"or "Y":
        st.add(inp)
        return 1
    else:
        return 2

def CreateSet():
    cmd=str(input("Are you sure Y/N"))
    if cmd=="y"or "Y":
        global st2
        st2= set(input("Enter element in set"))
        return 1
    else:
        return 2

def UnionSet(st,st2):
    if len(st2)==0:
        return 3
    cmd=str(input("Are you sure Y/N"))
    if cmd=="y"or "Y":
        print(st.union(st2))
        return 1
    else:
        return 2

def InterSet(st,st2):
    if len(st2)==0:
        return 3
    cmd=str(input("Are you sure Y/N"))
    if cmd=="y"or "Y":
        print(st.intersection(st2))
        return 1
    else:
        return 2

def DiffSet(st,st2):
    if len(st2)==0:
        return 3
    cmd=str(input("Are you sure Y/N"))
    if cmd=="y"or "Y":
        print(st.difference(st2))
        return 1
    else:
        return 2

def FrozenSet():
    cmd=str(input("Are you sure Y/N"))
    if cmd=="y"or "Y":
        global st
        st=frozenset(st)
        return 1
    else:
        return 2
