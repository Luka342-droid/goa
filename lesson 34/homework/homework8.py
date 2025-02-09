def sum_divisible_by_3():
    total = 0
    for num in range(1, 101):
        if num % 3 == 0:
            total += num
    return total

print(sum_divisible_by_3())
