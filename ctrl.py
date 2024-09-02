while True:
    x = input("Enter a number (or type 'exit' to quit): ")
    
    if x.lower() == 'exit':
        break 
    else:
        try:
            n = float(x)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue 

        if n > 0:
            print("The number is positive.")
        elif n < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")