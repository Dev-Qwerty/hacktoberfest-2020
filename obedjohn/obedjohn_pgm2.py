n=int(input("ENTER A DAY NUMBER IN RANGE 2 TO 365 "))
fdy=input("ENTER THE FIRST DAY OF YEAR ")
w=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
ws=[]
while len(ws)!=7:
    for a in w:
        if a==fdy and a not in ws:
            ws.append(a)
        if a not in ws:
            if a==fdy:
                break
            if fdy in ws:
                ws.append(a)
c=n%7
print("THE DAY ON THE DAY NUMBER ",n, "IS ",ws[c-1])
            
