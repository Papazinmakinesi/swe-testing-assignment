from quick_calc.calculator import Calculator

def run_cli():
    calc = Calculator()

    a = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if op == "+":
        result = calc.add(a, b)
    elif op == "-":
        result = calc.subtract(a, b)
    elif op == "*":
        result = calc.multiply(a, b)
    elif op == "/":
        result = calc.divide(a, b)
    else:
        print("Invalid operation")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    run_cli()