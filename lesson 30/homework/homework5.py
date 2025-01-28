#16) Count the number of times the word "the" appears in a given paragraph.
paragraph = "the quick brown fox jumps over the lazy dog and the dog barks"
print(paragraph.lower().count("the"))


#17) Ask the user to input a character and count its occurrences in a given string.
character = input("enter a character: ")
string = "hello world"
print(string.count(character))

#18) Create a function that counts and returns the occurrences of a specified word in a text.
def count_word_occurrences(text, word):
    print(text.lower().count(word))

text = "The quick brown fox and the lazy dog."
word = "the"
count_word_occurrences(text, word)
