# 7) Ask the user to enter a number multiple times and check if it's even or odd. Stop after 5 numbers.
for i in range(5):
    number = int(input("Enter a number: "))
    
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")



    
