class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y
   
    def subtract(self):
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        if self.y == 0:
            return "Division by zero(0) is invalid"
        return self.x // self.y

    def choice(self):
        while True:
            choice = int(input("Choose your method:\n1: Add\n2: Subtract\n3:Multiply\n4: Divide\n5: New inputs\n6: Exit\n"))
            if choice == 1:
                print(self.add())
            elif choice == 2:
                print(self.subtract())
            elif choice == 3:
                print(self.multiply())
            elif choice == 4:
                print(self.divide())
            elif choice == 5:
                self.x = int(input("Enter new x: "))
                self.y = int(input("Enter new y: "))
            elif choice == 6:
                print("bye bye")
                break
            else:
                print("you are a dick head clown")

calc = Calculator(10, 2)
calc.choice()
