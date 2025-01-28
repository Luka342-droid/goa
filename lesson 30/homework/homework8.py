#24) Verify if all the characters in a user-provided string are uppercase.
string = input("Enter a string: ")
print(string.isupper())

#25) Write a function that checks if a string consists entirely of uppercase letters and returns a boolean result.
def is_uppercase(text):
    return text.isupper()

print(is_uppercase("HELLO WORLD"))

#26) Check and display whether a string input by the user is in uppercase.
user_input = input("Enter a string to check: ")
print(user_input.isupper())
