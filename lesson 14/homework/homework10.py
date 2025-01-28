# მომხმარებლისგან სამი რიცხვის მიღება
num1 = int(input("შეიყვანეთ პირველი რიცხვი (num1): "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი (num2): "))
num3 = int(input("შეიყვანეთ მესამე რიცხვი (num3): "))

# დიაპაზონის შექმნა
range_values = range(num1, num2, num3)

# For ციკლით დიაპაზონის გადავლა და კვადრატების დაბეჭდვა
print("საიტერაციო ცვლადის კვადრატები:")
for value in range_values:
    print(value ** 2)
