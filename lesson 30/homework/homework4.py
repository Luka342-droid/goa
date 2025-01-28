#14) Find and print the length of a user-provided string.
user_string = input("Enter a string: ")
print(len(user_string))

#15) Write a function that takes a list of strings and returns their lengths.
def find_lengths(strings):
    for string in strings:
        print(len(string))

string_list = ["apple", "banana", "cherry"]
find_lengths(string_list)
