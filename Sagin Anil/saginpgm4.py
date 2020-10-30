# program to check if a number is an armstrong number or not

# get input
num = int(input("Enter a number: "))

sum = 0

# get the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# output result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
