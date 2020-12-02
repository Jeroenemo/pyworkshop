# Sort a list in reverse
lottery_numbers = [12, 54, 76, 37, 99]
sorted(lottery_numbers, reverse=True)

# sorted() will not alter original list
lottery_numbers.sort()

# OR
lottery_numbers.reverse()
# will.

# How to insert values into arbritrary position
# my_list(pos, value)
lottery_numbers.insert(0, 34)

# How to combine two lists together
names = ["Jeroen", "Hannah", "Jose", "Ninja"]
names.extend(lottery_numbers)

# How to check if value is in list
_in = "Jeroen" in names

# Check for index of value -- will only return first instance. 
_index = names.index("Hannah")

# Check how many times a value occurs 
_count = names.count("Attila")

# Update a value
names[0] = "Attila"

# if you dont know position if value
pos = names.index("Attila")
names[pos] = "Koji"


# remove value
names.remove("Hannah")
print(names)
return_value = names.pop(3)
print(return_value)