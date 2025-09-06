#Number of possible combinations from 0000 to 9999
combination = 10000

#Input from user(Number of guesses)
guess_num = eval(input("Please enter the number of guesses per second: "))

#calculation to crack the PIN per minute
crack_time = (1/guess_num) * (combination/60)

#Output to user(time to crack PIN)
print("Maximum time to crack the PIN:", round(crack_time, 3), "minutes")
