## Project 1: Lectures 1 - 5
# For this project we will be making a simple calculator
# For this calculator we will be using 
# - Python operators 
# - Python functions
# - Python function arguments
# - Python user defined functions

# The calculator will have the following functions for two variables:
# - Addition
# - Subtraction
# - Multiplication
# - Division 
# - Root of a number 
# - Exponentiation

## the main purpose of this project is to learn how to properly use functions and function arguments, and to learn how to organize a project with proper indentation

## ----- Note: this project will focus on the code and not UI-----------

def add (x, y): 
    return x+y
def substract (x, y):
    return x-y
def multiply (x, y): 
    return x*y
def div (x, y):
    return x/y
def sqr (x, y):
    num = x
    epsilon = 0.0025
    num_guess = 0
    guess = 0.0
    increment = 0.0001
    while abs(guess**y - x) >= epsilon and guess**y <= x:
        guess += increment
        num_guess += 1
    return guess
        #can also use x**(1/y) but we are using guess and check 
def exp (x, y):
    return x**y

print("Select Operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Finding the nth root")
print("6. Exponentiation")

while True: 
    action= input(" What computation would you like to proceed with? (make a selection from choices above 'e.g. 1'): ")
    if action in ('1', '2', '3', '4', '5', '6'):
        try: 
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
        except ValueError:
            print("Invalid entry")
            continue 
        if action == '1':
            print(f"{num1} + {num2} = {add(num1,num2)}")
        elif action == '2':
            print(f"{num1} - {num2} = {substract(num1,num2)}")
        elif action == '3': 
            print(f"{num1} x {num2} = {multiply(num1, num2)}")
        elif action == '4':
            print(f"{num1}/{num2} = {div(num1, num2)}")
        elif action == '5':
            print(f"{num2} root of {num1} = {sqr(num1, num2)} ")
        elif action == '6': 
            print(f" {num1} ** {num2} = {exp(num1, num2)}")
        
        next_calc= input("Want to do another calculation? (Yes/No): ")
        if next_calc == "No":
            print("Thank you for using my calculator!")
            break
        else: 
            print("Let's do another calculation!")
    else:
        print("invalid input")


