#21) Check if all characters in a given string are lowercase and print the result.
string = "hello world"
print(string.islower())

#22) Create a function that takes a string and returns True if it is completely in lowercase, otherwise False.
def is_lowercase(text):
    print(text.islower())

is_lowercase("hello world")

#23) Prompt the user to input a string and verify if it contains only lowercase letters.
user_input = input("Enter a string to check: ")
print(user_input.islower())
