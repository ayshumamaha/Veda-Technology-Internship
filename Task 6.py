def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one number.")
    if not any(not char.isalnum() for char in password):
        errors.append("Password must contain at least one special character.")

    return errors


def main():
    print("Simple Password Validator")
    password = input("Enter a password to validate: ")

    errors = validate_password(password)

    if errors:
        print("\nInvalid password:")
        for error in errors:
            print("- " + error)
    else:
        print("\nValid password! It meets all the requirements.")


if __name__ == "__main__":
    main()


# Examples:
# Valid: Strong@123
# Invalid: password
