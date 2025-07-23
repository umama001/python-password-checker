# This is a Python code for a Password Strength Checker.
# This project evaluates the strength of passwords based on various criteria.

import re # Import the 're' module for Regular Expressions. It helps in finding complex text patterns.

# --- Password Strength Check Function ---
# This function will actually check the strength of a password.
def check_password_strength(password):
    """
    Checks the strength of a given password based on several criteria.

    Returns:
        dict: Returns a dictionary containing the strength score and feedback.
    """
    score = 0 # The strength score of the password. A higher score means stronger.
    feedback = [] # A list of messages to tell users what's good or bad about their password.

    # Criteria 1: Length of the password
    if len(password) >= 12: # If the password is 12 or more characters long
        score += 2 # Add 2 points to the score.
        feedback.append("Password is a good length (12+ characters).") # Positive feedback.
    elif len(password) >= 8: # If the password is between 8 and 11 characters long
        score += 1 # Add 1 point to the score.
        feedback.append("Password is of moderate length (8-11 characters). Consider making it longer.") # Okay feedback, suggests improvement.
    else: # If the password is less than 8 characters long
        feedback.append("Password is too short. Aim for at least 8 characters, preferably 12+.") # Negative feedback, needs more length.

    # Criteria 2: Uppercase letters (A-Z)
    # re.search(r"[A-Z]", password) checks if the password contains any uppercase letter.
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Contains uppercase letters.") # Positive feedback.
    else:
        feedback.append("Consider adding uppercase letters.") # Suggests improvement.

    # Criteria 3: Lowercase letters (a-z)
    # re.search(r"[a-z]", password) checks if the password contains any lowercase letter.
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Contains lowercase letters.") # Positive feedback.
    else:
        feedback.append("Consider adding lowercase letters.") # Suggests improvement.

    # Criteria 4: Numbers (0-9)
    # re.search(r"\d", password) checks if the password contains any digit.
    # '\d' is a shortcut in regular expressions for digits.
    if re.search(r"\d", password):
        score += 1
        feedback.append("Contains numbers.") # Positive feedback.
    else:
        feedback.append("Consider adding numbers.") # Suggests improvement.

    # Criteria 5: Special characters (like !, @, #, $, %)
    # re.search(r"[!@#$%^&*()_+={}\[\]:;<>,.?/~`]", password) checks if the password contains any special character.
    # Many special characters need to be 'escaped' in regex (like \[\]{}), but here common ones are used directly.
    if re.search(r"[!@#$%^&*()_+={}\[\]:;<>,.?/~`]", password):
        score += 1
        feedback.append("Contains special characters.") # Positive feedback.
    else:
        feedback.append("Consider adding special characters (e.g., !@#$%^&*).") # Suggests improvement.

    # Optional additional complexity check: Three or more identical consecutive characters (e.g., 'aaa', '111')
    # re.search(r"(.)\1\1", password)
    # (.) -- Matches and captures any single character (except newline).
    # \1  -- Matches the SAME character that was captured first.
    # \1  -- Matches the SAME character again.
    # So, it looks for three identical characters in a row.
    if re.search(r"(.)\1\1", password):
        score -= 1 # Deduct a point if found, as it makes the password weaker.
        feedback.append("Warning: Contains 3 or more consecutive identical characters (e.g., 'aaa').") # Warning feedback.

    # Determine the overall strength based on the total score.
    strength = "Very Weak" # Default strength.
    if score >= 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 2:
        strength = "Moderate"
    else: # If the score is less than 2.
        strength = "Weak"

    # Return all the information in a dictionary.
    return {"score": score, "strength": strength, "feedback": feedback}

# --- Main Function ---
# This function takes password input from the user and displays the results.
def main():
    print("--- Password Strength Checker ---") # Prints the program title.
    while True: # Runs a loop so the user can check multiple passwords.
        password = input("Enter a password to check (or 'q' to quit): ") # Asks the user for a password.
        if password.lower() == 'q': # If the user types 'q' (case-insensitive),
            print("Exiting Password Checker. Goodbye!") # Print goodbye message.
            break # Exit the loop, which stops the program.

        if not password: # If the user enters an empty input (no password).
            print("Error: Password cannot be empty. Please enter a password.")
            continue # Go back to the start of the loop to ask for a password again.

        results = check_password_strength(password) # Call the strength check function with user's password.

        # Display the results in a clear format.
        print(f"\nPassword Strength: {results['strength']} (Score: {results['score']})") # Show overall strength and score.
        print("Feedback:")
        for item in results['feedback']: # Loop through each item in the feedback list.
            print(f"- {item}") # Print each feedback message with a bullet point.
        print("-" * 30) # Prints a separator line for the next input.

# This is a standard Python block. It ensures that the 'main()' function runs only
# when this script is executed directly, not when it's imported into another file.
if __name__ == "__main__":
    main()
