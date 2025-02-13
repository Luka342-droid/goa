def no_duplicates(user_list):
    return list(set(user_list))

print(no_duplicates([1, 2, 3, 2, 1])) 
print(no_duplicates(['apple', 'banana', 'apple', 'orange'])) 
print(no_duplicates([10, 20, 30, 20, 10, 40])) 
