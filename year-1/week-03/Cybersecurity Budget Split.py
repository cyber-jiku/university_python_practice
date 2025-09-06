#Inputs from user(%, total budget)
budget_total = eval(input("Please enter the total budget: "))
Firewall_perc = eval(input("Please enter the % for Firewalls: "))
Training_perc = eval(input("Please enter the % for Training: "))
Incident_perc = eval(input("Please enter the % for Incident Response: "))

#Calculations for allocations
firewall_alc = budget_total * (Firewall_perc/100)
training_alc = budget_total * (Training_perc/100)
incident_alc = budget_total * (Incident_perc/100)

#Output allocations to user
print("Amount allocated for Firewalls:", firewall_alc)
print("Amount allocated for Training:", training_alc)
print("Amount allocated for Incident Response:", incident_alc)
