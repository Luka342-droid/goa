print("Welcome to Hangman!")

# მოთამაშე 1 ირჩევს სიტყვას
word = input("Player 1, enter a word: ").lower()
print("\n" * 50)  # ეკრანის გასუფთავება, რომ Player 2-მა ვერ დაინახოს სიტყვა

hidden_word = ["_"] * len(word)
attempts = 6

print("Player 2, start guessing!")
print(" ".join(hidden_word))

while attempts > 0 and "_" in hidden_word:
    guess = input("Guess a letter: ").lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left.")

    print(" ".join(hidden_word))

if "_" not in hidden_word:
    print("Congratulations! You guessed the word!")
else:
    print(f"Game Over! The word was '{word}'.")
