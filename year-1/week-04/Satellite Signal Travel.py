import math

h = 35786
c = 300000

#Input (degrees)
Q = float(input("Please enter the degrees: "))
rad_Q = math.radians(Q)

#Calculation (signal distance travelled)
d = h / math.sin(rad_Q)
latency_sec = d / c
latency_ms = latency_sec * 1000

#Output to user (distance, latency)
print("Signal travel distance:", round(d, 2), "km")
print("One-way latency:", round(latency_ms, 2), "ms")