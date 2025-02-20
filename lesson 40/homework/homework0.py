# 1. ეს ფუნქცია აბრუნებს სტრიქონს "hello world" ყოველ გამოძახებაზე.
def greet():
    return "hello world"

# 2. ფუნქცია იღებს სიას რომელიც შეიცავს True/False მნიშვნელობებს და ითვლის True-ების რაოდენობას.
def count_sheeps(sheep):
    return sheep.count(True)

# 3. ფუნქცია იღებს სტრიქონს და შლის ყველა ცარიელ ადგილს (space).
def no_space(x):
    return x.replace(" ", "")

# 4. ფუნქცია იღებს მთელ რიცხვს და აბრუნებს მის გაორმაგებულ მნიშვნელობას.
def double_integer(i):
    return i * 2

# 5. ფუნქცია იღებს სახელს და აბრუნებს პერსონალიზებულ მისალმებას.
def greet(name):
    return f"Hello, {name} how are you doing today?"

# 6. ფუნქცია იღებს ბულიურ (True/False) მნიშვნელობას და აბრუნებს მას სტრიქონად გარდაქმნილ სახით.
def boolean_to_string(b):
    return str(b)

# 7. ფუნქცია იღებს არითმეტიკულ ოპერატორს და ორ რიცხვს შემდეგ კი ასრულებს შესაბამის მათემატიკურ ოპერაციას.
def basic_op(operator, value1, value2):
    if operator == "+":  # შეკრება
        return value1 + value2
    elif operator == "-":  # გამოკლება
        return value1 - value2
    elif operator == "*":  # გამრავლება (შეცდომა იყო ""-ის გამოყენება)
        return value1 * value2
    else:  # გაყოფა
        return value1 / value2

# 8. ფუნქცია ითვლის რამდენი ლიტრი წყლის დალევა შეიძლება მოცემული საათების განმავლობაში (ყოველ 2 საათში 1 ლიტრი).
def litres(time):
    return time // 2  # // იყენებს მთელ გაყოფას

# 9. ფუნქცია იღებს რიცხვს გარდაქმნის სტრიქონად აბრუნებს შებრუნებულ ციფრებს სიაში.
def digitize(n):
    starting_str = str(n)  # რიცხვის სტრიქონად გარდაქმნა
    reversed_str = starting_str[::-1]  # შებრუნება
    res_list = []  # ახალი სიის შექმნა

    for i in reversed_str:  # თითოეული ციფრის გადატანა სიის ელემენტად
        res_list.append(int(i))
    return res_list

# 10. ფუნქცია იღებს მთელ რიცხვთა სიას და აბრუნებს ახალ სიას სადაც თითოეული ელემენტი გაორმაგებულია.
def maps(a):
    saver = []  # ახალი სია
    for i in a:
        saver.append(i * 2)  # გაორმაგება და სიაში დამატება
    return saver

# 11. ფუნქცია ამოწმებს ერთი ყვავილის ფურცლები კენტია თუ არა, ხოლო მეორის ლუწი.
# თუ ერთ-ერთი კენტია და მეორე ლუწი აბრუნებს True-ს (სიყვარულია) სხვა შემთხვევაში False-ს.
def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 == 1:  # პირველი ლუწი მეორე კენტი
        return True
    elif flower1 % 2 == 1 and flower2 % 2 == 0:  # პირველი კენტი მეორე ლუწი
        return True
    else:
        return False  # ორივე კენტი ან ორივე ლუწი

# 12. ფუნქცია იღებს რიცხვთა სიას და აბრუნებს მათ ჯამს.
def sum_array(a):
    return sum(a)  # sum() ფუნქცია ყველა ელემენტს აჯამებს
