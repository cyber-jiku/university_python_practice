alerts_per_min = 120
size_alert = 1.8

#Inputs from user(hours)
hours = float(input("Please enter the number of hours: "))

#Calculations
hours_to_min = hours * 60
number_of_alerts = hours_to_min * 120
size_of_alerts = number_of_alerts * size_alert
size_in_mb = size_of_alerts / 1024

#Output to user
print("Total space taken by alerts:", round(size_in_mb, 2), "MB")