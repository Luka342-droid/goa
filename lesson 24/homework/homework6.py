my_list = [10, 20, 30, 40, 50, 60]  # Example list (even length)
midpoint = len(my_list) // 2  # Calculate the midpoint

first_half = my_list[:midpoint]  # First half
second_half = my_list[midpoint:]  # Second half

print("First half:", first_half)
print("Second half:", second_half)
