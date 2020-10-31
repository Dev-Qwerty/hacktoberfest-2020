# Python program to find the sum of natural using recursive function
#example 3 so the program is gonna take 3 + 2 + 1 and return 6 as the output
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num =int(input("enter your number"))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
