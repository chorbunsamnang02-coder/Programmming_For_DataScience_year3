def letter_grade(score):
    if score >= 97 and score <= 100:
        return " Grade A+"
    elif score >= 90 and score < 97:
        return " Grade A"
    elif score >= 80 and score < 90:
        return " Grade B"
    elif score >= 70 and score < 80:
        return " Grade C"
    elif score >= 60 and score < 70:
        return " Grade D"
    elif score >= 0 and score < 60:
        return " Grade F"
    else:
        return" invalid grade"
#### part A
for score in [99, 90, 85.5, 72, 60, 59.9, -5, 101]:
    print(score, "->", letter_grade(score))


### Part B

# because if we write condition A before A+ then the condition A+ will never be reached since A is already true for scores 97 and above. 
# Therefore, we need to check for A+ first before checking for A.