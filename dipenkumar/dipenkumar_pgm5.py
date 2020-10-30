# ARMSTRONG NUMBER  -- 3/9
num = int(input("Enter a number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10  # TO EXTRACT LAST DIGIT
    sum += digit**3   # TO REPEATEDLY ADD
    num //= 10
if temp == sum:
    print("The number is Armstrong.")
else:
    print("The number is not Armstrong.")
