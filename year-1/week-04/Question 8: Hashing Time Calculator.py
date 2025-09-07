hash_per_sec = 2500000

#Input from user (number of hash to compute)
hashtocompute = int(input("Enter the number of hash to compute: "))

#Calculations
time_sec = hashtocompute / hash_per_sec
time_min = time_sec / 60

#Output to user (time taken in seconds and minutes)
print("Time taken to hash:", round(time_sec ,2), "s")
print("Time taken to hash:", round(time_min ,2), "minute(s)")
