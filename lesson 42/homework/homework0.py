# 3
person = {
    "name": "Anna",
    "age": 25,
    "city": "New York",
    "job": "Engineer",
    "hobby": "Reading"
}
print(person.keys())

# 4
print(person.values())

# 5
print(person.items())

# 6
for key, value in person.items():
    print(f"{key}: {value}")

# 7
if "age" in person:
    print("Key 'age' exists in the dictionary")

# 8
print(person.get("job", "Not Found"))
print(person.get("salary", "Not Found"))

# 9
person["salary"] = 50000
print(person)

# 10
person.pop("hobby")
print(person)

# 11
new_info = {"city": "Los Angeles", "phone": "123-456-7890"}
person.update(new_info)
print(person)

# 12
print(len(person))

# 13
def sum_numeric_values(d):
    return sum(value for value in d.values() if isinstance(value, (int, float)))

print(sum_numeric_values(person))

# 14
person.clear()
print(person)

# 15
my_info = {
    "name": "luka",
    "surname": "amashukeli",
    "age": 13,
    "city": "tbilisi",
    "country": "geogia",
    "hobby": "basketball",
    "profession": "yes",
    "fav_language": "Python",
    "married": False,
    "height_cm": 154
}
print(my_info)
