import re

def password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search("[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search("[@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    return score, suggestions


password = input("Enter your password: ")
score, suggestions = password_strength(password)

if score <= 2:
    print("Strength: Weak ❌")
elif score <= 4:
    print("Strength: Medium ⚠️")
else:
    print("Strength: Strong ✅")

if suggestions:
    print("\nSuggestions to improve:")
    for s in suggestions:
        print("-", s)
