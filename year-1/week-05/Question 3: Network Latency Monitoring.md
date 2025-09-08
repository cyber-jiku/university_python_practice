## Question 3 – Network Latency Monitoring

Suppose you are monitoring network latency.  

- If the **ping response time** is more than **200 ms**, and the **packet loss** is above **2%**, an alert must be triggered.  

### Task  
Write a program that:  
1. Accepts the ping response time and packet loss as input from the user.  
2. Uses a Boolean condition to print `"Network unstable"` if **both thresholds** are exceeded, and `"Network stable"` otherwise.
