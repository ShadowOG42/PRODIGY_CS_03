import re

def assess_password_strength(password):
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    strength_score = sum(strength_criteria.values())
    
    if strength_score == 5:
        strength = "Strong"
    elif strength_score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    feedback = []
    if not strength_criteria["length"]:
        feedback.append("Increase the length to at least 8 characters.")
    if not strength_criteria["uppercase"]:
        feedback.append("Include at least one uppercase letter.")
    if not strength_criteria["lowercase"]:
        feedback.append("Include at least one lowercase letter.")
    if not strength_criteria["digit"]:
        feedback.append("Include at least one digit.")
    if not strength_criteria["special"]:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")
    
    return strength, feedback

if __name__ == "__main__":
    while True:
        password = input("Enter a password to assess: ")
        strength, feedback = assess_password_strength(password)
        
        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions to improve your password:")
            for tip in feedback:
                print(f"- {tip}")
        
        print("\nOptions:")
        print("1. Re-enter a new password")
        print("2. Exit")
        
        choice = input("Choose an option (1 or 2): ")
        if choice == "2":
            print("Exiting...")
            break
