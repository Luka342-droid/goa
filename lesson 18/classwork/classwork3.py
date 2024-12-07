num1 = int(input("შეიყვანეთ პირველი რიცხვი (num1): "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი (num2): "))

if num1 > num2:
    even_numbers = [x for x in range(num2, num1 + 1) if x % 2 == 0]
    print("ლუწი რიცხვები:", even_numbers)
    total_sum = sum(even_numbers)
else:
    odd_numbers = [x for x in range(num1, num2 + 1) if x % 2 != 0]
    print("კენტი რიცხვები:", odd_numbers)
    total_sum = sum(odd_numbers)

print("რიცხვების ჯამი:", total_sum)
