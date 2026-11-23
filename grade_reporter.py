
# PLP Python Week 3 - Grade Reporter

# List of learners' scores
scores = [72, 45, 90, 61, 38]

# Initialize counters and total
passed = 0
failed = 0
total = 0

# Loop through every score
for score in scores:

    # Determine the grade
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # Print the score and grade
    print(f"Score: {score} - Grade: {grade}")

    # Count passes and failures
    if score >= 50:
        passed += 1
    else:
        failed += 1

    # Add the score to the running total
    total += score

# Calculate the average
average = total / len(scores)

# Display the final report
print("\n----- GRADE REPORT -----")
print(f"Number of learners who passed: {passed}")
print(f"Number of learners who failed: {failed}")
print(f"Average score: {round(average, 1)}")