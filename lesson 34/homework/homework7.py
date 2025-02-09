def get_positive_numbers(list):
    positive_list =[]
    for num in list:
        if num > 0:
            positive_list.append(num)
    return positive_list

print(get_positive_numbers([-10, 15, -3, 7, 0, 22, -5]))
