#Input from user(role, time)
role = input("Enter your role (employee/manager/admin): ")
time = int(input("Enter the current time(0-23):"))

#Access logic
if time < 9 and time <17:
    print("Access Granted")
elif time >= 18 and (role == "manager" or role == "admin"):
    print("Access Granted")
else:
    print("Access Denied")
