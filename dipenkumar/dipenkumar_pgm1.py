num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
opr = input("Enter operator [+,-,*,/]:")
if opr == '+':
    result = num1+num2
elif opr == '-':
    result = num1-num2
elif opr == '*':
    result = num1*num2
elif opr == '/':
    result = num1/num2
else:
    print("Invalid Operartor")
print(num1, opr, num2, "=", result)
