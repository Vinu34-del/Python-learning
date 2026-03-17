l = [1, 23, 43, 534, 32]
total = 0

for sum in l:
    total = total + sum
print(total)

# ex-2
l2 = [1, 2, 3, 4, 5]
l3 = []

for num in l2:
    l3.append(num * 2)
    print(l3)

# ex-3:Printing food items
foods = ["Dosa", "Vada", "Idli"]
for items in foods:
    print(f"I like {items}")

# Looping through dictinories
student_marks = {"Anand": 87, "Geetha": 67, "Kumar": 98}
for student, marks in student_marks.items():
    print(f"{student} - {marks}")

# range
students = [
    "Vinay",
    "Nagu",
    "darshh",
]
marks = [25, 60, 40]
student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]
    print(student_marks)


# List comprehension
list_4 = [1, 2, 3, 4, 5]
dl = [item * 2 for item in list_4]
print(dl)

# same example but sqaure even number
list_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edl = [x * 2 for x in list_5 if x % 2 == 0]
print(edl)  # [4, 8, 12, 16, 20]


# Dictionary comprehension
names = {"Chandu", "Jaan", "Rahul"}
d = {name: len(name) for name in names}
print(d)  # {'Jaan': 4, 'Rahul': 5, 'Chandu': 6}

# ex-2
city_population = {"Bengaluru": 75, "Mysuru": 88, "Hubballi": 50, "Mangluru": 60}

large_cities = {key: value for key, value in city_population.items() if value > 80}
print(large_cities)  # {'Mysuru': 88}

# Splitting String to Create List
s = "This is a python"
result = s.split()
print(result)  # ['This', 'is', 'a', 'python']

# list input
print("List input practise")
x = input("Enter the list of integers: ").split()
dl = [int(num) for num in x]
print(dl)
