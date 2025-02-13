# 2) Tuple Indexing & Slicing
my_tuple = (10, 20, 30, 40, 50)
print("Second element:", my_tuple[1])    
print("Last element:", my_tuple[-1])     
print("Middle three elements:", my_tuple[1:4])  
# 3) Tuple Immutability
my_tuple[1] = 99 

# 4) Tuple Packing & Unpacking
packed_tuple = ("Alice", 25, "Engineer")
name, age, profession = packed_tuple 
print("Name:", name)
print("Age:", age)
print("Profession:", profession)

# 5) Tuple Methods
repeated_tuple = (1, 2, 3, 2, 2, 4, 5)
print("Count of 2:", repeated_tuple.count(2))
print("First occurrence of 3:", repeated_tuple.index(3)) 

# 6) Set Creation & Basic Operations
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  
my_set.remove(3) 
print("Set after modifications:", my_set)
print("Is 4 in the set?", 4 in my_set) 
# 7) Set Union & Intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)   
print("Intersection:", set1 & set2) 
print("Difference (set1 - set2):", set1 - set2) 

# 8) Removing Duplicates
dup_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(dup_list)  
unique_list = list(unique_set) 
print("List after removing duplicates:", unique_list)
