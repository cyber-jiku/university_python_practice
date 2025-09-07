import math

#Input from user (radius in meters)
radius = float(input("Please enter the radius in meters: "))

#Calculation
area = math.pi * (radius**2)

#Output to user (Area in square meters)
print("The area is:", round(area,2), "square meters.")
