t1=int(input("PLEASE ENTER THE FIRST TIME "))
t2=int(input("PLEASE ENTER THE SECOND TIME "))
if t1>t2:
    if t1%100==00:
        t1=int(str(t1//100-1)+'60')
    diff=t1-t2
else:
    if t2%100==00:
        t2=int(str(t2//100-1)+'60')
    diff=t2-t1
m=diff%100
h=diff//100
print("THE DIFFERENCE IS ",h, "HOURS & ",m, "MINUTES")
