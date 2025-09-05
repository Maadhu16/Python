# Nested if - if inside another if (used for checking multiple related conditions)

# Example:

marks = 85
attendance = 80

if marks >= 50:                # First check 
    if attendance >= 75:       # Second check if first condition is true
        print("Pass")
    else:
        print("Fail due to low attendance")
else:
    print("Fail due to low marks")

Output => Pass
