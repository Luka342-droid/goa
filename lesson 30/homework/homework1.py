#5) Convert all the characters of a given sentence to lowercase and print it.
sentence = "HI"
print(sentence.lower())


#6) Ask the user for their email address and ensure it is stored in lowercase.
email = input("enter your email address: ").lower()
print("Stored email:", email)


#7) Write a function that takes a mixed-case string and returns it in all lowercase letters.
def to_lowercase(text):
    print(text.lower())

mixed_case_string = "PyThOn Is FuN!"
to_lowercase(mixed_case_string)

def to_lowercase(text):
    print(text.lower())

# Example usage:
mixed_case_string = "PyThOn Is FuN!"
to_lowercase(mixed_case_string)  # Output: "python is fun!"
