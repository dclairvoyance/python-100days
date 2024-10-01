active = True
operators = ["+", "-", "*", "/"]

def eval(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("What's the first number? "))

while active:
    operator = input("Pick an operation: ")
    while operator not in operators:
        print("Invalid.")
        operator = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    # result = eval(num1, operator, num2)
    result = operators[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {result}")

    again = input("Type 'y' to continue calculating with %f, or type 'n' to start a new calculation: " % result)
    while again != "y" and again != "n":
        print("Invalid.")
        again = input("Type 'y' to continue calculating with %f, or type 'n' to start a new calculation: " % result)
    active = True if again == "y" else False
    num1 = result