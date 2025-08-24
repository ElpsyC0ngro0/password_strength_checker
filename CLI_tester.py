import re
import random
import string

# Function to check password strength
def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[@$!%*?&._-]", password) is None

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

    total_issues = sum([length_error, digit_error, uppercase_error, lowercase_error, special_char_error])

    if total_issues == 0:
        strength = "Strong"
    elif total_issues <= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, tips if total_issues > 0 else None

# Generate a random strong password
def generate_strong_password(length=14):
    chars = string.ascii_letters + string.digits + "@$!%*?&._-"
    while True:
        pw = ''.join(random.choice(chars) for _ in range(length))
        strength, _ = check_strength(pw)
        if strength == "Strong":
            return pw

# Main function
def main():
    print("Password Strength Checker & Multi Strong Password Generator")

    # Step 1: Get password from user
    password = input("\nEnter your password to check: ")

    # Step 2: Check strength
    strength, tips = check_strength(password)
    print(f"\nStrength: {strength}")
    if tips:
        print("\nTips to improve your password:")
        for tip in tips:
            print(tip)

    # Step 3: Offer to generate multiple passwords
    choice = input("\nDo you want me to generate strong password suggestions for you? (yes/no): ").strip().lower()
    if choice in ("yes", "y"):
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                print("[!] Password length too short. Using minimum length of 8.")
                length = 8
        except ValueError:
            print("[!] Invalid input. Using default length of 14.")
            length = 14

        count = random.randint(5, 10)  # Randomly choose between 5–10 suggestions
        print(f"\nHere are {count} randomly generated strong passwords ({length} characters each):")
        for i in range(count):
            print(f"{i+1}. {generate_strong_password(length)}")

if __name__ == "__main__":
    main()
