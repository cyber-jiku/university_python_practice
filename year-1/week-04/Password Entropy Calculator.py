import math

#Inputs from User (password length, number of possible symbols)
length = eval(input("Please enter the length of the password: "))
sym_num = eval(input("Please enter the number of possible symbols: "))

#Calculating entropy
Entropy = length * math.log2(sym_num)

#Output strength of password
print("Strength of password is:", Entropy)