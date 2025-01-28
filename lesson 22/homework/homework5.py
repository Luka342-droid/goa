words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
result = []
for i in range(0, len(words), 2):
    result.append(words[i])
print("Every second element:", result)
