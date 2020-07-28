def calculator(num1, num2, op):
    if (not (type(num1) == float or type(num1) == int) or not (type(num2) == float or type(num2) == int)):
        return "Please enter a number"
    if op == '-':
        return f"{num1} - {num2} = {num1 - num2}"
    if op == '+':
        return f"{num1} + {num2} = {num1 + num2}"
    if op == '*':
        return f"{num1} * {num2} = {num1 * num2}"
    if op == '/':
        return f"{num1} / {num2} = {num1 / num2}"
    else:
        return "Unknown operation"


# Addition
result = calculator(5, 2, '+')
print(result)

# Substruction
result = calculator(5, 2, '-')
print(result)

# Division
result = calculator(5, 2, '/')
print(result)

# Multiplication
result = calculator(5, 2, '*')
print(result)

# Unknown operation
result = calculator(5, 2, "unknown")
print(result)

# Not a number
result = calculator("num", 2, "-")
print(result)
