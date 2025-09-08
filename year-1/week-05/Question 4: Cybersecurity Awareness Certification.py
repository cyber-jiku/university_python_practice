#Input from user (number of session attended and final test score)
session = int(input("Enter the number of session attended: "))
final_score = float(input("Enter the final test percentage score: "))

#Certification Logic
if session == 5 or final_score >= 80:
    print("Certified")
else:
    print("Not Certified")
