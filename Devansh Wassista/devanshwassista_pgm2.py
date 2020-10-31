import os
import sys
filename='D:\\iss\\student.txt'
def insert():
    if os.path.isfile(filename):
        f=open(filename,'a')
        print('Enter Student Record')
        ch1='y'
        while ch1=='y' or ch1=="Y":
            rno=input("Enter the Roll number: ")
            name=input('Enter the name: ')
            subj=input("Enter the subject: ")
            rec=rno+'\t'+name+'\t'+subj
            f.write(rec+'\n')
            ch1=input('Do you want to insert again? ')
            if ch1=='y' or ch1=="Y":
                continue
            else:
                break
    else:
        print('File does not exist')
def display():
    if os.path.isfile(filename):
        print('Student records')
        f= open(filename,'r')
        dl=f.readline()
        while dl:
            print(dl,end='')
            dl=f.readline()
        f.close()
    else:
        print('File Does not Exist')
    f.close()
def searching():
    if os.path.isfile(filename):
        f=open(filename,'r')
        rno=int(input('Enter the Roll Number'))
        flag=True
        for k in f:
            i=0
            str1=''
            while True:
                if k[i]=='\t':
                    break
                if k[i]>='0' and k[i]<='9':
                    str1 += k[i]
                    i += 1
            str2 = int(str1)
            if rno == str2:
                print('Student found : ',k,end='')
                flag = True
                break
            if flag == False:
                print('Record doesnt exist')
    else:
        print('File Does Not Exist')
        f.close()
def quitting():
    sys.exit()
ch='y'
while ch=='y' or ch=='Y':
    sel = int(input(''' Enter your choice
                    1. Insert Record
                    2. Display Record
                    3. Search Record
                    4. Save and Quit
                    Any other input is invalid!!!'''))
    if sel==1:
        insert()
    if sel==2:
        display()
    if sel==3:
        searching()
    if sel==4:
        quiting()
    else:
        print('Invalid Input')
        
