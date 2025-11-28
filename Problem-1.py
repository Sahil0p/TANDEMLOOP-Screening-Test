# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string


class Calculator:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.op = ""

    def get_input(self):
        self.a = float(input("Enter first number: "))
        self.b = float(input("Enter second number: "))
        self.op = input("Enter operation (add / sub / mul / div): ").strip().lower()

    def solve(self):
        if self.op == "add":
            return self.a + self.b
        elif self.op == "sub":
            return self.a - self.b
        elif self.op == "mul":
            return self.a * self.b
        elif self.op == "div":
            if self.b == 0:
                return "Error: Cannot divide by zero"
            return self.a / self.b
        else:
            return "Invalid operation"

def main():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Perform Calculation")
        print("2. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calc = Calculator()
            calc.get_input()
            print("Result:", calc.solve())

        elif choice == "2":
            print("Exiting... Goodbye!")
            break
         
        else:
            print("Invalid choice! Try again.")

main()
