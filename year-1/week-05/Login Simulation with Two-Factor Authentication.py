#Input from user(username, password, if 2FA was successful)
user = input("Enter your username: ")
password = input("Enter your password: ")
success_2fa = input("Was 2FA successful?: ")

#Login Authentication Logic
if (user == "admin" and password == "admin000") and (success_2fa == "yes"):
    print("Login Successful")
else:
    print("Access Denied")