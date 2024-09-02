# Take two numbers as input from the user
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# Check the parity of both numbers using relational and logical operators
if n1 % 2 == 0 and n2 % 2 == 0:
    print("Both numbers are even.")
elif n1 % 2 != 0 and n2 % 2 != 0:
    print("Both numbers are odd.")
else:
    print("One number is even, and the other is odd.")