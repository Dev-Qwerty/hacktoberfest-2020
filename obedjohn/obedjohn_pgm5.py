def Bsearch(ar,item):
    beg=0
    last=len(ar)-1
    while beg<=last:
        mid=(beg+last)//2
        if item==ar[mid]:
            return mid
        elif item<ar[mid]:
            last=mid-1
        else:
            beg=mid+1
    else:
        return False
n=int(input("ENTER THE LENGTH OF LINEAR LIST: "))
ar=[0]*n
print("ENTER THE ELEMENTS FOR LINEAR LIST IN ASCENDING ORDER")
for i in range(n):
    ar[i]=int(input("ELEMENT "+str(i)+": "))
item=int(input("ENTER THE ELEMENT TO BE SEARCHED: "))
index=Bsearch(ar,item)
if index:
    print("ELEMENT FOUND AT INDEX ",index, "POSITIONED AT ",index+1)
else:
    a="ELEMENT FOUND AT INDEX " + str(index)+ " POSITIONED AT " + str(index+1)
    if a=="ELEMENT FOUND AT INDEX False POSITIONED AT 1":
        print("ELEMENT NOT FOUND")
    else:
        print(a)
