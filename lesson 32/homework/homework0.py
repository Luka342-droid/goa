# Task 3
def welcome_message(name, age):
    print(f"Welcome {name}, age {age}!")

# Task 4
def format_name(first_name, last_name):
    first_name_formatted = first_name[0].upper() + first_name[1:].lower() if first_name else ""
    last_name_formatted = last_name[0].upper() + last_name[1:].lower() if last_name else ""
    print(first_name_formatted + " " + last_name_formatted)

# Task 5
def reverse_string(sentence):
    reversed_str = ""
    for char in sentence:
        reversed_str = char + reversed_str
    print("The reversed string is: " + reversed_str)

# Task 6
def insert_word(sentence, word, index):
    words = sentence.split()
    result = []
    current_index = 0
    for w in words:
        if current_index == index:
            result.append(word)
        result.append(w)
        current_index += 1
    if current_index <= index: 
        result.append(word)
    output = ""
    for w in result:
        output += w + " "
    print(output.strip())

# Task 7
def sentence_to_words(sentence):
    word = ""
    words = []
    for char in sentence:
        if char == " ":
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)
    print(words)

# Task 8
def csv_to_list(csv_string):
    item = ""
    items = []
    for char in csv_string:
        if char == ",":
            items.append(item)
            item = ""
        else:
            item += char
    items.append(item)
    print(items)

# Task 9
def paragraph_to_sentences(paragraph):
    sentence = ""
    sentences = []
    for char in paragraph:
        if char == ".":
            sentences.append(sentence.strip())
            sentence = ""
        else:
            sentence += char
    if sentence.strip():
        sentences.append(sentence.strip())
    print(sentences)

# Task 10
def append_item(lst, item):
    new_list = []
    for i in lst:
        new_list.append(i)
    new_list.append(item)
    print(new_list)

# Task 11
def append_items(lst, items):
    new_list = []
    for i in lst:
        new_list.append(i)
    for item in items:
        new_list.append(item)
    print(new_list)

# Task 12
def append_all_elements(list1, list2):
    new_list = []
    for i in list1:
        new_list.append(i)
    for j in list2:
        new_list.append(j)
    print(new_list)

# Task 13
def insert_item(lst, index, item):
    new_list = []
    current_index = 0
    for i in lst:
        if current_index == index:
            new_list.append(item)
        new_list.append(i)
        current_index += 1
    if current_index <= index:  
        new_list.append(item)
    print(new_list)

# Task 14
def insert_at_beginning(lst, item):
    new_list = [item]
    for i in lst:
        new_list.append(i)
    print(new_list)

# Task 15
def insert_at_end(lst, item):
    new_list = []
    for i in lst:
        new_list.append(i)
    new_list.append(item)
    print(new_list)

