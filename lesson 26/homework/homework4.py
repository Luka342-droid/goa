def find_maximum(numbers):
    if not numbers:
        return None
    return max(numbers)

numbers = [3, 4, 7, 2, 8, 5]
print(find_maximum(numbers))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(6))