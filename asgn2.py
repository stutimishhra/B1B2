import os
import time
from time import sleep as pause

#PROBLEM 1
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

print(greet("Pooh"))
print(greet("Pooh", "Good evening,"))

print("---------")

#PROBLEM 2
def create_profile(*, name, age=18, city):
    return f"Name: {name}, Age: {age}, City: {city}"

print(create_profile(name="Pooh", age=21, city="Jaipur"))
print(create_profile(name="Jai", city="Gurgaon"))

print("---------")

#PROBLEM 3
def sum_numbers(*args, **kwargs):
    total = sum(arg for arg in args if isinstance(arg, (int, float)))
    return (total, kwargs)
    
print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 2, x=4, y=5))

print("---------")

#PROBLEM 4
def square_list(numbers):
    return list(map(lambda x: x**2, numbers))

print(square_list([11, 12, 13, 14]))

print("---------")

#PROBLEM 5
def filter_odd_numbers(numbers):
    return list(filter(lambda x: x%2==0, numbers))

print(filter_odd_numbers([1, 2, 3, 4]))

print("---------")

#PROBLEM 6
squares = [x**2 for x in range(5)]

print(squares)

print("---------")

#PROBLEM 7
even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print("Even numbers in the given range are: ",even_numbers)

print("---------")

#PROBLEM 8
def file_operations():
    # Create a directory named "test_folder"
    os.makedirs("test_folder", exist_ok=True)
    print("Directory 'test_folder' created.")
    
    # Pause the execution for 3 seconds
    time.sleep(3)
    
    # Remove the directory named "test_folder"
    os.rmdir("test_folder")
    print("Directory 'test_folder' deleted.")

# Example usage
file_operations()

print("---------")

#PROBLEM 9

# Pause for 2 seconds
pause(2)  
print("Paused execution!")

print("---------")

#PROBLEM 10
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            # If the item is a list, recursively flatten it
            flat_list.extend(flatten_list(item))
        else:
            # If the item is not a list, append it to flat_list
            flat_list.append(item)
    return flat_list

# Example usage
print(flatten_list([1, [2, 3], [[4, 5], 6]]))  

print(flatten_list([[1, 2], [3, [4, [5]]]])) 