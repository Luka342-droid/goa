my_list = ['ელემენტი1', 'ელემენტი2', 'ელემენტი3', 'ელემენტი4', 'ელემენტი5', 'ელემენტი6', 'ელემენტი7', 'ელემენტი8', 'ელემენტი9', 'ელემენტი10']
user_input = int(input("შეიყვანეთ რიცხვი: "))
list_length = len(my_list)

if 0 <= user_input and user_input < list_length:
    print("ინდექს " + str(user_input) + "-ზე მყოფი ელემენტია: " + my_list[user_input])
elif -list_length <= user_input and user_input <= -1:
    print("უარყოფით ინდექს " + str(user_input) + "-ზე მყოფი ელემენტია: " + my_list[user_input])
else:
    print("მითითებული რიცხვი სიის დიაპაზონს სცდება.")
