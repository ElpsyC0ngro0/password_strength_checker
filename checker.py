import re

def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[@$!%*?&._-]", password) is None

    # Collect feedback tips
    tips = []
    if length_error:
        tips.append("-> Use at least 8 characters.")
    if digit_error:
        tips.append("-> Include at least one digit (0–9).")
    if uppercase_error:
        tips.append("-> Add at least one uppercase letter (A–Z).")
    if lowercase_error:
        tips.append("-> Add at least one lowercase letter (a–z).")
    if special_char_error:
        tips.append("-> Include a special character (@ $ ! % * ? & . _ -)")

    # Count total issues
    total_issues = sum([length_error, digit_error, uppercase_error, lowercase_error, special_char_error])

    # Determine strength
    if total_issues == 0:
        strength = "Strong"
    elif total_issues <= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, tips if total_issues > 0 else None

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    strength, tips = check_strength(password)
    print(f"\nStrength: {strength}")

    if tips:
        print("\nTips to improve your password:")
        for tip in tips:
            print(tip)

if __name__ == "__main__":
    main()

