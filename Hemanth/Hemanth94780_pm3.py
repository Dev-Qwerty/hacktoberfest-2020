#Program to check if a number is amstrong number or not
NUM=int(input("Enter a number : "))
TEMP=NUM
SUM=0
while (NUM>0):
    DIGIT=NUM%10
    SUM+=DIGIT**3
    NUM=NUM//10
if (TEMP==SUM):
    print("Amstrong Number")
else:
    print("Not Amstrong Number")
    
