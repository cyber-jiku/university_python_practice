log = 2.5

#Inputs from user (seconds)
sec = float(input("Please enter the amount of seconds for which you wish to display the size of logs: "))

#Calculations
size = log * (2** sec)

#Output to user
print("Log size after t seconds: ", round(size,3), "MB")
