num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("answer =", num1 + num2)

elif operator == "-":
    print("answer =", num1 - num2)

elif operator == "*":
    print("answer =", num1 * num2)

elif operator == "/":
    print("answer =", num1 / num2)

else:
    print("invalid operator")