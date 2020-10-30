def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("1) ADD\n2) SUBTRACT\n3) MULTIPLY\n4) DIVIDE")
ch=int(input())
a=int(input("ENTER FIRST NUMBER "))
b=int(input("ENTER SECOND NUMBER "))
if ch==1:
    print(add(a,b))
elif ch==2:
    print(subtract(a,b))
elif ch==3:
    print(multiply(a,b))
elif ch==4:
    print(divide(a,b))
else:
    print("INVALID CHOICE")
