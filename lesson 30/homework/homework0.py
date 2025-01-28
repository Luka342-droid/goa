# 2) Convert a given sentence to uppercase and print the result.
sentence = "hello"
print(sentence.upper())

# 3) Take a user's name input and display it in uppercase letters:
name = input("Enter your name: ")
print("Your name in uppercase:", name.upper())

#4) Create a function that converts a list of lowercase strings to uppercase:
def convert_to_uppercase(words):
    uppercase_words = [word.upper() for word in words]
    print(uppercase_words)

lowercase_words = ["apple", "banana", "cherry"]
convert_to_uppercase(lowercase_words)  