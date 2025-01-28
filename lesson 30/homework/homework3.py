#11) Find the position of the first occurrence of the word "Python" in a sentence.
sentence = "I am learning Python programming."
print(sentence.find("Python"))


#12) Search for a user-specified substring in a provided string and print its starting index.
text = input("Enter a string: ")
substring = input("Enter a substring to search for: ")
print(text.find(substring))

#13) Write a function to find and return the index of a specified character in a given string.
def find_index(text, char):
    print(text.find(char))

string = "hello world"
character = "o"
find_index(string, character)
