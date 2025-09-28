num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
match operation:
    case "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    case "-":
        result = num1 - num2    
        print(f"The result of {num1} - {num2} is {result}")
    case "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}") 
        else:
            print("Error: Division by zero is not allowed.")
