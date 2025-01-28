my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num1 = int(input("შეიყვანეთ პირველი მთელი რიცხვი (num1): "))
num2 = int(input("შეიყვანეთ მეორე მთელი რიცხვი (num2): "))

if num1 > num2:
    new_list = my_list[num2:num1]
elif num2 > num1:
    new_list = my_list[num1:num2]
else:
    new_list = []

print("ახალი სია:", new_list)
