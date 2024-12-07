correct_password = "my_secret_password" 

attempts = 0

while True:
    user_input = input("შეიყვანეთ პაროლი: ") 
    attempts += 1 
    if user_input == correct_password:
        print("Access granted!")
        print("თქვენ {attempts} მცდელობა დაგჭირდათ.")
        break  
    else:
        print("პაროლი არასწორია, სცადეთ თავიდან.")
