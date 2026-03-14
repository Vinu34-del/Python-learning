# Tuple
fruits = ("Apple", "Banana", "Cherry")
numbers = (1, 2, 3, 4)
print(fruits)
print(numbers)

# Accessing tuple item
print(fruits[1])  # Banana
print(fruits[-1])  # Cherry

# Slicing
print(fruits[0:2])  # ('Apple', 'Banana')

# Tuple operation
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
final_tuple = first_tuple + second_tuple
print(final_tuple)

# Tuple repetation
number = (1, 2) * 3
print(number)

# Tuple methods
print(number.count(1))  # 3
print(number.index(2))  # 1

# Set()
s = {30, 50, 20}
print(s)  # {50, 20, 30} - Unordered

# Create empty set()
empty_set = set()

# Set operations
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# 1.Union
print(s1 | s2)  # {1, 2, 3, 4, 5}

# 2.Intersection
print(s1 & s2)  # {3}

# 3.Diffrence
print(s1 - s2)  # {1, 2}

# Set Methods
s3 = {7, 8, 9}

# add()
s3.add(10)
print(s3)  # {8, 9, 10, 7}

# remove()
s3.remove(7)
print(s3)  # {8, 9, 10}

# discard()
s3.discard(21)
print(s3)  # no error is popped

# pop()
s3.pop()
print(s3)  # {9, 10}

# clear()
s3.clear()
print(s3)  # set()
