password = "mypassword"
user_password = input("Enter the password: ")

while user_password !=password:
    print("Incorrect password, try again.")
    user_password = input("Enter the password: ")

print("Password correct, access granted!")
