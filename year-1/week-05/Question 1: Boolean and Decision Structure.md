## Boolean and Decision Structure Exercises  

Execute the following expressions in the **Shell** section of Thonny and observe the outcomes.  
Pay attention to **operator precedence** while evaluating them:  

```python
# a.
x = 5
y = 10
x == y  # Checks if x and y are equal

# b.
a = 7
b = 7
a != b  # Checks if a and b are NOT equal

# c.
score = 85
passing_score = 90
score < passing_score  # Checks if score is less than passing_score

# d.
is_raining = True
has_umbrella = True
is_raining and not(has_umbrella)  # True only if it is raining AND you don't have an umbrella

# e.
is_sunny = False
is_warm = True
is_sunny or is_warm  # True if it is sunny OR warm (or both)

# f.
age = 25
has_ticket = True
is_vip = False
age >= 18 and has_ticket or is_vip
# True if (age is 18 or older AND has a ticket) OR is a VIP
