def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        

        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
    except ValueError:
        print("Invalid input! Please enter numerical values.")

calculator()