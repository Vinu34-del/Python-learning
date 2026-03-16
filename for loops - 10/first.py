# for loop
city = ["Mysore", "Banglore", "Hasan", "Sirsi"]
for cities in city:
    print(cities)

#range
for i in range(1,11):
    print(i,end=" ")

# step
for i in range(1,26,2):
    print(i,end=" ")

#looping over string
name = "Vinay"
for letter in name:
    print(letter)

# enumerate
name = "Chandan"
for index, letter in enumerate(name):
    print(letter*(index+1))

# using dict
d = {"name": "Vinay", "age": 21, "income": 1}
for key, value in d.items():
    print(key, " ", value)

# nested for loop
for i in range(2, 11):
    for j in range(1, 11):
        print(f"{i}X{j} = {i*j}")
