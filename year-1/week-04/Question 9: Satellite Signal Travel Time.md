## 🛰️ Question 9 – Satellite Signal Travel Time

A security agency communicates with satellites at an altitude of **35,786 km**.  
The distance travelled by the signal depends on the satellite's elevation angle `θ` (in degrees) and is given by:

**d = h / sin(θ)**

Where:  
- `h` = satellite altitude  
- `θ` = elevation angle  

📌 **Task:**  
Write a Python program that:  
1. Asks the user to enter `θ` (in degrees)  
2. Calculates:
   - The signal travel distance `d`  
   - The one-way latency in **milliseconds**, assuming signal speed = `300,000 km/s`  

💡 **Hint:** Use `math.radians(angle_degrees)` to convert degrees to radians.  
