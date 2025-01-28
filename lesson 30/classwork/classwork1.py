def manual_find(main_string, str_to_find):
    main_length = 0
    while main_string[main_length:main_length+1] != "":
        main_length += 1

    find_length = 0
    while str_to_find[find_length:find_length+1] != "":
        find_length += 1

    i = 0
    while i <= main_length - find_length:
        j = 0
        while j < find_length and main_string[i + j] == str_to_find[j]:
            j += 1

        if j == find_length:
            return i
        
        i += 1

    return -1

print(manual_find("hello world", "world"))
