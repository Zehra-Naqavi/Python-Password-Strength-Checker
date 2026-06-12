import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters required")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("💡 12+ characters makes it much stronger")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z)")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")

    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")

    # Symbol check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one symbol (!@#$%^&*...)")

    # Strength rating
    if score <= 2:
        strength = "Weak"
        emoji = "🔴"
    elif score <= 4:
        strength = "Moderate"
        emoji = "🟡"
    elif score == 5:
        strength = "Strong"
        emoji = "🟢"
    else:
        strength = "Very Strong"
        emoji = "✅"

    return score, strength, emoji, feedback


def main():
    print("=" * 40)
    print("   🔐 Password Strength Checker")
    print("=" * 40)
    print()

    while True:
        password = input("Enter a password to check (or 'quit' to exit): ")

        if password.lower() == 'quit':
            print("\nGoodbye!")
            break

        if not password:
            print("Please enter a password.\n")
            continue

        score, strength, emoji, feedback = check_password_strength(password)

        print()
        print(f"Score:    {score}/6")
        print(f"Strength: {emoji} {strength}")
        print()

        if feedback:
            print("Suggestions:")
            for tip in feedback:
                print(f"  {tip}")
        else:
            print("✅ Your password meets all requirements!")

        print()
        print("-" * 40)
        print()


if __name__ == "__main__":
    main()
