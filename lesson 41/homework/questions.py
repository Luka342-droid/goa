
import random
# question
questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 5 + 7?", "12"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("Who wrote 'Hamlet'?", "Shakespeare"),
    ("What is the square root of 64?", "8"),
    ("What is the chemical symbol for water?", "H2O"),
    ("How many continents are there on Earth?", "7"),
    ("What is the largest mammal in the world?", "Blue whale"),
    ("Which gas do plants absorb from the atmosphere?", "Carbon dioxide"),
    ("What year did the Titanic sink?", "1912")
]

random.shuffle(questions)
score = 0
# user answer
for question, answer in questions:
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is:", answer)

print(f"Your score: {score}/{len(questions)}")
