n=k=5
i=1
while i<=n:
    j=1
    while j<=n:
        if j >= k: 
            print( "*", end=" ") 
        else:
            print(" ", end=" ") 
        j+=1
    print()
    k-=1
    i+=1
