first = float(input("enter the first number: "))
second = float(input("enter the second number: "))
operation = input("enter an operation(+, -, *, /): ")
 
if operation == "+":
    result = first + second
elif operation == "-":
    result = first - second
elif operation == "*":
    result = first * second
elif operation == "/":
    if second != 0:
      result = first / second
    else:
      result = "Error: Division by zero"
else:
   result = "Invalid expectation"
print(f"Result: {first} {operation} {second} = {result}")
