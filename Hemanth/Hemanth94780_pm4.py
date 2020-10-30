#Program to check leap year
year=int(input("Enter year to check leap year or not"))
if year%400==0:
    print("leap year")
elif year%100==0:
    print("Not leap year")
elif year%4==0:
    print("Leap year")
else:
    print("Not leap year")
