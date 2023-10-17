class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y



cal = Calculator()

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

addition = cal.add(a, b)
print(f"{a} + {b} = {addition}")

subtraction = cal.subtract(a, b)
print(f"{a} - {b} = {subtraction}")

multiplication = cal.multiply(a, b)
print(f"{a} * {b} = {multiplication}")

division = cal.divide(a, b)
print(f"{a} / {b} = {division}")

