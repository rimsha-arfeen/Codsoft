def add(x,y):
    res=x+y
    print("addition of",x ,"and",y,"is=",res)
def sub(x,y):
    res=x-y
    print("the subtraction of",x,"and",y,"is =",res)
def mul(x,y):
    res=x*y
    print("multiplication of",x,"and",y,"is =",res)
def div(x,y):
        res=x//y
        print("the result is:",res)
def mod(x,y):
    res=x%y
    print("the mod division of ",x,"and",y,"is=",res)
print("********************CALCULATOR********************")
print("The following are the choices of operations performed by this calculator\n")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulo Division\n")
print("**************************************************")
x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
ch=int(input("Enter your choice:"))
if ch==1:
     add(x,y)
elif ch==2:
     sub(x-y)
elif ch==3:
     mul(x,y)
elif ch==4:
     div(x,y)
elif ch==5:
     mod(x,y)
else:
     exit     