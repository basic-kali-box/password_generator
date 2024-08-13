from password_generator import generate



website = input("Which website ? ")


user = input("Enter your Username / address : ")


symbol = input("Wanna Use symbol Y/N : ") 

AL = (
    'abcdefghijklmnopqrstuvwxyz' + \
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
    '01234567890'
)
AB = (
    'abcdefghijklmnopqrstuvwxyz' + \
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
    '01234567890' + \
    '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
)



if symbol == 'y' or symbol=='Y' :
	password = generate(chars=AB)
else :
	password = generate(chars=AL)


print("Your Password is : "+ password)



