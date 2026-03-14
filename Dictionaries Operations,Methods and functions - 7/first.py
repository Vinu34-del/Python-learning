# Dictinory
birthday = {"Vinay": "04-07-2025", "Darshan": "27-05-2005", "Virat": "02-10-2005"}
print(birthday)

# Accessing dict element
print(birthday["Vinay"])  # 04-07-2005

# safe access
print(birthday.get("Sudeep", "Not found"))  # Not found

# Adding and Updating Dictionary Elements
birthday["Sudeep"] = "02-09-1973"
print(
    birthday
)  # {'Vinay': '04-07-2005', 'Darshan': '27-05-2005', 'Virat': '02-10-2005', 'Sudeep': '02-09-1973'}

birthday["Vinay"] = "04-07-2005"
print(birthday)

# Removing element from the dict
x = birthday.pop("Virat")
print(x)

# Delete using dell keyword
del birthday["Virat"]
print(birthday)

# Dictonary Methods

# 1.keys()
print(birthday.keys())  # (['Vinay', 'Darshan', 'Virat'])

# 2.values()
print(birthday.values())  # (['04-07-2025', '27-05-2005', '02-10-2005'])

# 3.items()
print(
    birthday.items()
)  # dict_items([('Vinay', '04-07-2025'), ('Darshan', '27-05-2005'), ('Virat', '02-10-2005')])
