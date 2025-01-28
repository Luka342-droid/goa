def manual_index(main_string, search_string):
    main_length = 0
    search_length = 0

    for _ in main_string:
        main_length += 1

    for _ in search_string:
        search_length += 1

    for i in range(main_length):
        j = 0
        while j < search_length and i + j < main_length and main_string[i + j] == search_string[j]:
            j += 1
        if j == search_length:
            return i 

    return -1 

print(manual_index("hello world", "world"))  # 6
print(manual_index("hello world", "hello"))  # 0
print(manual_index("hello world", "abc"))    # -1
