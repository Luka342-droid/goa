import random
# player 1
print("Welcome to 'Guess the Number'!")
print("Player 1, enter a secret number between 1 and 100 (it will be hidden).")

number = int(input())  
print("\n" * 50) 

attempts = 0
guess = None 
# 2 player guessing 
print("Player 2, guess the number!")

while guess != number: 
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    
print(f"Congratulations! You guessed it in {attempts} attempts.")
