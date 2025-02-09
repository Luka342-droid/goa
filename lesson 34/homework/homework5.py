def check_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print("even")
        else:
            print("odd")

check_numbers([10, 15, 22, 37, 40])
