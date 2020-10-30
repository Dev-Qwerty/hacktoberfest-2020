# TO CHECK WHETHER NUMBER IS PALINDROME OR NOT -- 1/9
num = int(input("Enter the number: "))
temp = num   # STORES INPUT NUMBER IN TEMP WITHOUT CHANGING NUMBERS VALUE
Reverse = 0.
while(num > 0):
    Reminder = num % 10  # ANY NUMBER % 10 WILL GIVE LAST DIGIT
    Reverse = (Reverse * 10) + Reminder
    num = num // 10
print("The Reverse of number is", int(Reverse))
if temp == Reverse:      # COMPARES ORIGNAL VALUE WITH REVERSED VALUE
    print("The number is plaindrome.")
else:
    print("The number is not plaindrome.")
