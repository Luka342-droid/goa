# 8) Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords.

incorrect_count = 0

correct_password = "Goa best"
password = ""

while password != correct_password:
    password = input("Enter the password: ")

    if password != correct_password:
        incorrect_count += 1 
        print("Incorrect password. Try again.")
        
print("Incorrect password attempts: " + str(incorrect_count))
