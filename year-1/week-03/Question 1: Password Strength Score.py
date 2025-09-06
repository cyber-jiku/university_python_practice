#User inputs (Password Length, Number of Special Characters)
password_len = eval(input("Please enter the password length: "))
special_num = eval(input("Please enter the number of special characters: "))

#Password Strength Score
password_score = (password_len * 5) + (special_num * 10)

#Output to user (Password Strength Score)
print("Password Strength Score:", password_score)
