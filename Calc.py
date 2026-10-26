class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        remainder = abs(a) % abs(b)
        return -remainder if a < 0 else remainder

    def power(self, a, b):
        if a == 0 and b < 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a**b
