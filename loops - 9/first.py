# Loops
is_failed = True
i = 1

while is_failed:
    if i % 2 != 0:
        i = i + 1
        continue  # using continue
    print(f"Try {i}")
    i = i + 1
    if i >= 100:
        break  # using break
print("I gave up")

# example
i = 0
while i <= 10:
    print(i)
    i = i + 1

# ATM PIN
pin = "1234"
trails = 0

while trails < 3:
    input_pin = input(f"Trail-{trails} pin: ")
    trails = trails + 1
    if input_pin == pin:
        print("CORRECT")
        break
    else:
        print("INCORRECT")
