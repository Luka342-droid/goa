def count_occurrences(main_str, str_to_count):
    count = 0
    i = 0
    while main_str[i:i + 1] != "":  # main_str სიგრძის პოვნა
        j = 0
        while str_to_count[j:j + 1] != "":  # str_to_count სიგრძის პოვნა
            j += 1
        str_to_count_length = j

        if main_str[i:i + str_to_count_length] == str_to_count:
            count += 1
        i += 1
    print(count)

main_str = input("შეიტანეთ მთავარი სტრიქონი: ")
str_to_count = input("შეიტანეთ დასათვლელი სტრიქონი: ")

count_occurrences(main_str, str_to_count)
