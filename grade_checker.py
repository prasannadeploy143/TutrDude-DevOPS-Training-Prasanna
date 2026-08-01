# Take score input from the user and convert it to an integer
score = int(input("Enter your score: "))

# Check the grade based on the score ranges
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
