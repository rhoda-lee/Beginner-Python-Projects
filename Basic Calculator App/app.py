def add(num1, num2):
    result = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(result))

def subtract(num1, num2):
    result = num1 - num2
    print(str(num1) + " - " + str(num2) + " = " + str(result))

def multiply(num1, num2):
    result = num1 * num2
    print(str(num1) + " * " + str(num2) + " = " + str(result))

def divide(num1, num2):
    result = num1 / num2
    print(str(num1) + " / " + str(num2) + " = " + str(result))


print("A. Add")
print("B. Subtract")
print("C. Myltiply")
print("D. Divide")
print("E. Exit")

user_choice = input("Enter alphabet associated with the operation you want to perform: ")

if user_choice == "a" or user_choice == "A":
    print("Addition")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    add(num1, num2)
elif user_choice == "b" or user_choice == "B":
    print("Subtraction")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    subtract(num1, num2)
elif user_choice == "c" or user_choice == "C":
    print("Multiplication")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    multiply(num1, num2)
elif user_choice == "d" or user_choice == "D":
    print("Division")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    divide(num1, num2)
elif user_choice == "e" or user_choice == "E":
    print("Exit")
    quit()