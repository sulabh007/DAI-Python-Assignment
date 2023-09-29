##def function(a,b,c=10):
##    a=a+c
##    b=b+c
##    return a+b+c
##print(function(a=10,b=10))


##count=0
##def f1():
##    global count
##    count=count+1
##    print(f"you called f1 function {count} times")
##
##f1()
##f1()
##f1()
##f1()


##def f1():
##    x=34
##    print(x)
##    def f2():
##        #global x
##        nonlocal x
##        x=45
##        print(x)
##    print(x)
##    f2()
##    print(x)
##
##x=10
##print(x)
##f1()
##print(x)

##x=5
##print(x, bin(x))
##y=9
##print(y, bin(y))
##newnum=x<<4
##newx=newnum|y
##print(int(newx),bin(newx))
##
##y1=newx&(int(0b1111))
##print("y1",y1,"y",y)
##print("x1",newx>>4,"x",x)

##s="THIS IS STRING"
##print(s[::-1])
##print(s[::1])
##print(s[2:-2:1])



s1="this is a cat, cat is cute, where is you r cat? mine is here"

pos=len(s1)

while pos!=-1:
	pos=s1.rfind("cat",0,pos-1)
	print(pos)

	
##pos=s1.find("cat")
##print(pos)
##pos=s1.find("cat",pos+1)
##print(pos)
##pos=s1.find("cat",pos+1 )
##print(pos)
##pos=s1.find("cat",pos+1 )
##print(pos)
##print("*"*69)
##pos=s1.rfind("cat",pos+1 )
##print(pos)
##pos=s1.rfind("cat",pos+1 )
##print(pos)
##pos=s1.rfind("cat",pos+1 )
##print(pos)
##pos=s1.rfind("cat",pos+1 )
##print(pos)


	
##print("*"*69)
##i=len(s1)-1;
##s=0
##while(i>=0):
##	pos=s1.find("cat", i)
##	if(pos!=s) and pos!=-1:
##		print(pos)
##		s=pos
##	i=i-1
