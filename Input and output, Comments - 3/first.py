#  Input and Output in py
print("Python")  # output

age = input("Age: ")  # Input
print(age)

# concatination usnig input
boy_name = input("Boy Name: ")
boy_age = int(input("Boy Age: "))
girl_name = input("Girl Name: ")
girl_age = int(input("Girl Age: "))
age_diff = boy_age - girl_age

print(boy_name + " Loves " + girl_name + ". Age difference is " + str(age_diff))
print(f"{boy_name} loves {girl_name}. Age diffrence is {age_diff}")  # Formated string
