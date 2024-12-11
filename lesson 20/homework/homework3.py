# 6) Use a loop to calculate the sum of numbers between two given integers.
# Input two integers
start = int(input("Enter the starting integer: "))
end = int(input("Enter the ending integer: "))

total_sum = 0
for i in range(start, end + 1):
    total_sum += i

print("The sum of numbers between", start, "and", end, "is:", total_sum)
