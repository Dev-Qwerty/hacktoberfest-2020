#program to convert km to mph
# Get KM imput
kilometers = float(input("Enter value in kilometers: "))

# the conversion factor
conv_fac = 0.621371

# calculating miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
