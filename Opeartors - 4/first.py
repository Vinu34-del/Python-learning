# Operators

# Assignment Op
a = 10
a += 20  # a = a + 20
a *= 10
a -= 2
print(a)

# Comparision Op
A = 20
B = 10
print(A == B)
print(A != B)
print(A < B)
print(A > B)
print(A > B)
print(A != B)


x = 5
y = 10
z = 15

# and operator
print(x > 0 and y > 5)  # Output: True (both conditions are True)

# or operator
print(x > 10 or z > 10)  # Output: True (one of the conditions is True)

# not operator
print(not (x > 10))  # Output: True (reverses False to True)

# Membership Op
my_list = [1, 2, 3, 4, 5]
my_string = "Python"
print("P" in my_string)  # True
print(3 not in my_list)  # False
print(not ("y" in my_string))  # False (Reverse)

# Bitwise Op
a = 5  # In binary: 101
b = 3  # In binary: 011

# Bitwise AND
print(a & b)  # Output: 1 (binary: 001)

# Bitwise OR
print(a | b)  # Output: 7 (binary: 111)

# Bitwise XOR
print(a ^ b)  # Output: 6 (binary: 110)

# Bitwise NOT
print(~a)  # Output: -6 (inverts all bits)

# Left shift
print(a << 1)  # Output: 10 (binary: 1010)

# Right shift
print(a >> 1)  # Output: 2 (binary: 010)
