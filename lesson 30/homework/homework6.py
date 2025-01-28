#19) Find and print the index of the first occurrence of the word "hello" in a given string.
string = "hello world not hello"
print(string.find("hello"))

#20) Write a function that returns the index of a character provided by the user in a string.
def find_char_index(text, char):
    print(text.find(char))

user_char = input("Enter a character: ")
string_to_search = "hello world"
find_char_index(string_to_search, user_char)
