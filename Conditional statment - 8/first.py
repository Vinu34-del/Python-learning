# Conditional statment

# if
x = 2
if x % 2 == 0:
    print("X is Even")

# if-else
x = 4
if x % 2 == 0:
    print("X is Even")
else:
    print("X is odd")

# elif
signal = "Red"
if signal == "Red":
    print("STOP")
elif signal == "Yellow":
    print("READY")
else:
    print("GO")

# Example
time = 10

if time == 8:
    print("It's a breakfast time!")
elif time == 1:
    print("It's a lunch time !")
elif time == 10:
    print("It's a dinner time !")
else:
    print("It's not a meal time!")

# Logical Op
att = 74
teacher_frd = True

if (att >= 75) or teacher_frd:
    print("EXAM")
else:
    print("NO EXAM")

# Example
gender = input("Enter your gender: ")
age = int(input("Enter your age: "))

if gender == "female":
    print("Free ticket")
else:
    if age <= 5:
        print("Ticket is free.")
    elif age <= 12:
        print("You get a child discount. Half ticket")
    elif age >= 60:
        print("You get senior citizen discount.")
    else:
        print("Pay the full price")
