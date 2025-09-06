#Time taken to encrypt per character in seconds
encrypt_time = 0.005

#Inputs from user (Length of message)
char_num = eval(input("Please enter the message length: "))

#Calculation of encryption
encryption_sec = char_num * encrypt_time

#Output time taken to user in seconds
print("Encryption time:", encryption_sec, "seconds")
