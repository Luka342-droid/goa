import random

my_num = random.randint(1, 10) 

attempts = 0

while True:
    user_input = input("გამოიცანით რიცხვი (1-დან 10-მდე): ") 
    if user_input.isdigit():
        user_guess = int(user_input) 
        attempts += 1 
        
        if user_guess == my_num:  
            print("You guessed!") 
            print("თქვენ {attempts} მცდელობა დაგჭირდათ.")
            break 
        else:
            print("არასწორი, სცადეთ თავიდან.")
    else:
        print("გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")
