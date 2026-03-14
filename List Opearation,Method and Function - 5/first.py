# List
items = ["Bruh", "Sugar", "Milk","Bruh2"]
mix_data = [23, "Vinay", True]
print(items)
print(mix_data)

# Example for accessing element form the list
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])  # Apple
print(fruits[-1])  # Cherry

# Modifying list

# Changing specific element
fruits[1] = "Orange"
print(fruits)

# Adding element:

# 1.append()
fruits.append("Kivi")
print(fruits)

# 2.insert()
fruits.insert(0, "Graphs")
print(fruits)

# Removing element

# 1.remove()
fruits.remove("Cherry")
print(fruits)

# 2.pop()
fruits.pop()
print(fruits)

# Slicing
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])
print(numbers[:4])
print(numbers[3:])
print(numbers[::2])

# Function
number_2 = [2,5,3,1,7]
print(len(number_2)) #5
print(sorted(number_2)) #[1, 2, 3, 5, 7]
print(sum(number_2)) #18

# Methods
number_3 = [1,4,2,1,2]
print(number_3.index(4)) #1
print(number_3.count(2)) #2
number_3.reverse()
print(number_3) #[2, 1, 2, 4, 1]
number_3.sort()
print(number_3) #[1, 1, 2, 2, 4]

# Nested list
matrix = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]
print(matrix[1][0])  # 4
