import getpass
import string

# Function to check the strength of a password
def check_password(password):

    score = 0
    feedback = []

    # Check Length
    if len(password)>=12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 12 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    #Check for numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Check for common passwords
    common_passwords = ["password", "123456", "123456789", "qwerty", "abc123", "password1", "111111", "admin123", "password123"]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("Password is too common. Avoid using common passwords.")

    #Check for repeated characters
    if len(set(password)) < len(password) / 2:
        score -= 1
        feedback.append("Password has too many repeated characters. Try to use more unique characters.")

    #Check for sequential characters
    sequential = False
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i]) + 2 == ord(password[i + 2]):
            sequential = True
            break
    if sequential:
        score -= 1
        feedback.append("Password contains sequential characters. Avoid using sequences like 'abc' or '123'.")

    #Score judgment
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, feedback

    #Feedback
    '''if feedback:
        print("\nFeedback:")
        for recommendation in feedback:
            print(f"- {recommendation}")'''

# Main function to run the password auditor
'''print("Welcome to the Password Auditor!")
password = getpass.getpass("Please enter your password for auditing: ")
check_password(password)

print("\nAudit Complete. Thank you for using the Password Auditor!")'''
