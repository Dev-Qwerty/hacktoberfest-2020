# QUADRATIC EQUATION
# ax**2+bx+c=0    a!=0
import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b*b-4*a*c
if a == 0:
    print("The value of 'a' should not be zero.")
else:
    if d > 0:
        r1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        r2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
        print("The roots are real")
        print(f"The Roots are {r1} and {r2}.")
    elif d == 0:
        r1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        r2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        print("The root are equal.")
        print(f"The Roots are {r1} and {r2}.")
    else:
        print("The roots are complex and imaginary.")
