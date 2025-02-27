car = {
    'make': 'Toyota',
    'model': 'Corolla',
    'year': 2020,
    'color': 'blue',
    'price': 20000
}


print("Keys in the dictionary:")
for key in car.keys():
    print(key)

print("Values in the dictionary:")
for value in car.values():
    print(value)

print("Key-value pairs in the dictionary:")
for key, value in car.items():
    print(f"{key}: {value}")

print("Formatted key-value pairs:")
for key, value in car.items():
    print(f"The {key} of the car is {value}.")
