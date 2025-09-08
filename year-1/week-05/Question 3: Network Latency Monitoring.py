#Input from user(ping, packet loss)
ping = float(input("Enter ping response time in ms: "))
per_loss = float(input("Enter packet loss percentage: "))

#Logic
if ping > 200 and per_loss > 2:
    print("Network Unstable")
else:
    print("Network Stable")
