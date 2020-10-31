def mergefile(a,b,):
    import os
    f1="D:\\iss\\"+a
    f2="D:\\iss"+b
    if os.path.isfile(f1) and os.path.isfile(f2):
        f1=open(f1,'r')
        f2=open(f2,'r')
        fw=open('D:\\iss\\New.dat','w+')
        f1read=f1.read()
        fw.write(f1read)
        f2.readline()
        for c in f2:
            fw.write(c)
        fw.flush()
        fw.seek()
        d=fw.read()
        print(d)
    else:
        print('File Doesnt exist ')
file1='file1'
file2='file2'
mergefile(file1,file2)
            
