# Phishing Email Detection (Rule-Based Model)
# No external libraries required

phishing_keywords = [
    "urgent", "verify", "click", "winner", "free",
    "lottery", "bank", "account", "password", "reset",
    "limited", "offer", "confirm"
]

def detect_phishing(email):
    email = email.lower()
    score = 0

    for word in phishing_keywords:
        if word in email:
            score += 1

    if score >= 2:
        return "Phishing"
    else:
        return "Safe"

# -----------------------------
# Dataset
# -----------------------------
emails = [
    "Congratulations you won a lottery click here",
    "Urgent verify your bank account now",
    "Meeting scheduled tomorrow",
    "Please find the attached report",
    "Reset your password immediately",
    "Lunch meeting at 1 PM"
]

labels = ["Phishing", "Phishing", "Safe", "Safe", "Phishing", "Safe"]

# -----------------------------
# Prediction & Accuracy
# -----------------------------
correct = 0
predictions = []

for i in range(len(emails)):
    result = detect_phishing(emails[i])
    predictions.append(result)
    if result == labels[i]:
        correct += 1

accuracy = correct / len(emails)

# -----------------------------
# Confusion Matrix
# -----------------------------
tp = fp = tn = fn = 0

for i in range(len(emails)):
    if labels[i] == "Phishing" and predictions[i] == "Phishing":
        tp += 1
    elif labels[i] == "Safe" and predictions[i] == "Safe":
        tn += 1
    elif labels[i] == "Safe" and predictions[i] == "Phishing":
        fp += 1
    elif labels[i] == "Phishing" and predictions[i] == "Safe":
        fn += 1

print("Accuracy:", accuracy)
print("\nConfusion Matrix")
print("[[TP:", tp, " FP:", fp, "]]")
print("[[FN:", fn, " TN:", tn, "]]")

# -----------------------------
# Test New Email
# -----------------------------
test_email = input("\nEnter email text to check: ")
print("Email Classification:", detect_phishing(test_email))
