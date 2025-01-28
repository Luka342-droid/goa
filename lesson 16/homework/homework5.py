username = "user123"
password = "mypassword"

username = input("Enter username: ")
password = input("Enter password: ")

while username != username or password != password:
    print("Incorrect username or password, try again.")
    username = input("Enter username: ")
    password = input("Enter password: ")

print("Username and password correct, access granted!")
