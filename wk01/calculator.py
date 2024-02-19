import math
class Calculator:
    def __init__(self):
        self.home()

    def home(self):
        print("Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Sine")
        print("6. Cosine")
        print("7. Tangent")
        print("8. Cosecant")
        print("9. Exit")
        response = input("Please enter an option: ")
        try: 
            option = int(response)
            options = [
                self.add, self.subtract, self.multiply, self.divide,
                self.sine, self.cosine, self.tangent, self.cosecant, self.close
            ]
            options[option-1]() #this calls the methods
        except ValueError:
            print("Wrong input, must be a number between 1 and 9")
            self.home()

    def add(self):
        print("Adding")
        first = input("Enter a number: ")
        second = input("Enter another number: ")
        try:
            answer = float(first) + float(second)
            print(first, "+", second,"=", answer)
        except :
            print("Wrong input")
            self.home()
            return

    def subtract(self):
        print("Subtracting")
        first = input("Enter a number: ")
        second = input("Enter another number: ")
        try:
            answer = float(first) - float(second)
            print(first, "-", second, "=", answer)
        except :
            print("Wrong input")
            self.home()
            return

    def multiply(self):
        print("Multiplying")
        first = input("Enter a number: ")
        second = input("Enter another number: ")
        try:
            answer = float(first) * float(second)
            print(first, "*", second, "=", answer)
        except :
            print("Wrong input")
            self.home()
            return

    def divide(self):
        print("Dividing")
        first = input("Enter a number: ")
        second = input("Enter another number: ")
        try:
            answer = float(first) / float(second)
            print(first, "/", second, "=", answer)
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except :
            print("Wrong input")
            self.home()
       
            return
        
    def cosine(self):
        print("Calculating Cosine")
        angle = input("Enter an angle in degrees: ")
        try:
            answer = math.cos(math.radians(float(angle)))
            print("cos(", angle, ") =", answer)
        except :
            print("Wrong input")
            self.home()
       
        return
        
    def tangent(self):
        print("Calculating Tangent")
        angle = input("Enter an angle in degrees: ")
        try:
            answer = math.tan(math.radians(float(angle)))
            print("tan(", angle, ") =", answer)
        except :
            print("Wrong input")
        except ZeroDivisionError:
            print("Tangent is undefined for this angle")
            self.home()
       
            return

    def sine(self):
        print("Calculating Sine")
        angle = input("Enter an angle in degrees: ")
        try:
            answer = math.sin(math.radians(float(angle)))
            print("sin(", angle, ") =", answer)
        except :
            print("Wrong input")
            self.home()
       
            return          

    def cosecant(self):
        print("Calculating Cosecant")
        angle = input("Enter an angle in degrees: ")
        try:
            sin_value = math.sin(math.radians(float(angle)))
            if sin_value == 0:
                raise ZeroDivisionError
            answer = 1 / sin_value
            print("csc(", angle, ") =", answer)
        except ValueError:
            print("Wrong input")
        except ZeroDivisionError:
            print("Cosecant is undefined for this angle")
            return


    def close(self):
        print("Exiting")
        return
    pass

Calculator()