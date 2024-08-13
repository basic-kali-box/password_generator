from password_generator import generate
import pyperclip

def get_password_length():
    while True:
        try:
            length = int(input("Enter the password length (default is 12): ") or 12)
            if length < 1:
                print("Password length must be at least 1.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")

def want_symbols():
    while True:
        response = input("Do you want to include symbols in your password? (Y/N): ").strip().lower()
        if response in {'y', 'n'}:
            return response == 'y'
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
""" if response in { 'y' , 'n'}
	if response =='y':
		return true
    	else : return false
    else :
        print("invalind input, please enter 'Y' or 'N'.")
"""
def save_to_file(website, user, password):
    filename = "passwords.txt"
    with open(filename, "a") as file:
        file.write(f"{website} | {user} | {password}\n")
    print(f"Password details have been saved to {filename}")

def main():
    print("Welcome to the Password Generator!")
    
    website = input("Which website? ").strip()
    user = input("Enter your Username / address: ").strip()
    include_symbols = want_symbols()
    length = get_password_length()
    
    AL = (
        'abcdefghijklmnopqrstuvwxyz' +
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
        '0123456789'
    )
    
    AB = (
        'abcdefghijklmnopqrstuvwxyz' +
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
        '0123456789' +
        '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
    )
    
    characters = AB if include_symbols else AL
    password = generate(length=length, chars=characters)
    pyperclip.copy(password)

    print(f"\nYour generated password for '{website}' and username '{user}' is:\n{password}")
    
    save_to_file(website, user, password)

if __name__ == "__main__":
    main()

