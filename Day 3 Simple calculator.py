print("***** Simple Calculator ***** \n")

num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))

add = num1 + num2
substraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {substraction}" )
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")