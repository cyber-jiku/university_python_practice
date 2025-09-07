combination = 10**6

#Inputs from user (number of guesses)
guess = int(input("Please enter the number of guesses: "))

#Calculation
time = (combination/guess) / (60*60)

#Output time taken to user
print("Maximum time in hours required to crack it:", round(time,3), "hours.")
