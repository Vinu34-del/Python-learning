# Functions
def greet():
    print("Hello Python")

greet()


# Function parameters

# Positional argument
def love(boy, girl):  # passing parameters
    print(f"Boy name is: {boy}")
    print(f"Girl name is: {girl}")
    print(f"{boy} Loves {girl}")

love("Ram", "Sita")  # function called
love("King", "Queen")


# Ex-1
def tabel(num):
    for i in range(1, 11):
        print(f"{num}X{i}={num*i}")

tabel(5)
tabel(10)
tabel(25)


# Returning value from a function
def func(num):
    return int(str(num) * 3)

a = 100
b = func(2)
c = a + b
print(c)


# Local and Global variable
def func():
    x = "Vinay"  # Local variable (inside a function)
    print("Hello")

y = "Darshhh"  # Global variable (Outside the function)
