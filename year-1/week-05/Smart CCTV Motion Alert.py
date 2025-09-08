#Input (motion detection status, time)
motion = input("Enter motion detection status(True/False): ")
time = float(input("Enter time (0-23): "))

#Alert Logic
if motion == "True" and time >= 22:
    print("Motion Alert: Possible Intrusion")
else:
    print("All clear")