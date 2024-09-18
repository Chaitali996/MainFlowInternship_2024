""" 
Write a Python program to create a list, a
dictionary, and a set. Perform basic operations
like adding, removing, and modifying
elements.
"""
# Creating a list
my_list = [1, 2, 3, "hello", "world"]

# Adding elements to the list
my_list.append(4)
my_list.insert(2, "new_element")

# Removing elements from the list
my_list.remove("hello")
del my_list[1]  # Removing element at index 1

# Modifying elements in the list
my_list[0] = "changed"

# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "Mumbai"}

# Adding elements to the dictionary
my_dict["occupation"] = "Engineer"

# Removing elements from the dictionary
del my_dict["city"]

# Modifying elements in the dictionary
my_dict["age"] = 31

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to the set
my_set.add(6)

# Removing elements from the set
my_set.remove(2)

# Sets do not allow duplicate elements, so adding a duplicate element will have no effect
my_set.add(3)

# Printing the results
print("List:", my_list)
print("Dictionary:", my_dict)
print("Set:", my_set)
