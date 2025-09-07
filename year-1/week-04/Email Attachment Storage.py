emails_hour = 250
per_email = 15 / 100
email_attach_size = 2

#Inputs from user (Number of hours)
hours = float(input("Please enter the number of hours: "))

#Calculation
total_emails = emails_hour * hours
total_attach_email = total_emails * per_email
total_size = total_attach_email * email_attach_size

sizeinGB = total_size / 1024

#Output to user (size in MB and GB)
print("Total space taken:", round(total_size,2), "MB")
print("Total space taken:", round(sizeinGB,2), "GB")