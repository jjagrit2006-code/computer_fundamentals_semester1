def add(a,b): 
    return a + b
def subtract(a,b): 
    return a - b
def multiply(a,b): 
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("=== Simple Calculator ===")
    while True:
        s = input("Enter first number (or q to quit): ").strip()
        if s.lower() == 'q':
            print("Goodbye.")
            break
        try:
            a = float(s)
        except:
            print("Invalid number. Try again.")
            continue
        try:
            b = float(input("Enter second number: ").strip())
        except:
            print("Invalid number. Restarting.")
            continue
        op = input("Operation (+ - * /): ").strip()
        if op == '+':
            print("Result:", add(a,b))
        elif op == '-':
            print("Result:", subtract(a,b))
        elif op == '*':
            print("Result:", multiply(a,b))
        elif op == '/':
            print("Result:", divide(a,b))
        else:
            print("Invalid operation.")
        print("-"*30)

if _name_ == "_main_":
    main()