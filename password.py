import secrets
import string

def generate_password(length, complexity):
    """
    Generates a random password of the specified length and complexity.
    
    :param length: The desired length of the password.
    :param complexity: The desired complexity level of the password.
    :return: A randomly generated password.
    """
    if complexity == 1:
        # Lowercase letters only
        alphabet = string.ascii_lowercase
    elif complexity == 2:
        # Lowercase and uppercase letters
        alphabet = string.ascii_letters
    elif complexity == 3:
        # Lowercase, uppercase letters, and digits
        alphabet = string.ascii_letters + string.digits
    elif complexity == 4:
        # Lowercase, uppercase letters, digits, and special characters
        alphabet = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose between 1 and 4.")
        return None
    
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    """
    Main function to run the password generator.
    """
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        complexity = int(input("Enter the desired complexity level of the password (1-4): "))
        if complexity < 1 or complexity > 4:
            print("Invalid complexity level. Please choose between 1 and 4.")
            continue
        
        password = generate_password(length, complexity)
        if password:
            print(f"Generated password: {password}")
            break

if __name__ == "__main__":
    main()
