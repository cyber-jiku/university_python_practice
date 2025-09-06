#Input from User(file size in bytes)
file_size = eval(input("Please enter the file size in bytes: "))

#Calculations to convert from bytes to kilobytes to megabytes
B_KB = file_size / 1024
KB_MB = B_KB / 1024

#Output to User (Size in KB and MB)
print("File size in KB:", B_KB)
print("File size in MB:", KB_MB)