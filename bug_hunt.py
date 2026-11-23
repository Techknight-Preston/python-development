
# PLP Python Week 3 - Bug Hunt

count = 1
total = 0

# BUG 1: Added the missing colon after the while condition.
# BUG 2: Changed < 5 to <= 5 to include number 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG 3: Converted total to a string to fix the TypeError.
print("Sum of 1 to 5 is: " + str(total))