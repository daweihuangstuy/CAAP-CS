# Dawei Huang
# 07/17/2018
# CAAP Computer Science Assignment 1

# Programs for Part 1 of the assignment is contained in the file hello.py
# Programs for Part 2 of the assignment is contained in the file cash.py

# Part 1

# Problem 1
print ("--------------------------------------------")
print ("This is Problem 1: Hello World\n")
print ("This program will print 'Hello!' in terminal")
print ("Hello!")
print ("--------------------------------------------")

# Problem 2
print ("--------------------------------------------")
print ("This is Problem 2: Convertor\n")
print ("This program will convert Fahrenheit to Celcius")
def fahToCel():
    fah = input("Please enter a valid temperature in Fahrenheit: ")
    cel = (float(fah) - 32.0)/ 1.8
    i = 1
    while i <= 5:
        print("Celcius: " + str(cel) + " degrees celcius ")
        i += 1
fahToCel()
print ("--------------------------------------------")

# Problem 3
print ("--------------------------------------------")
print ("This is Problem 3: Unit Conversion\n")
print ("This program will convert inches to centimeters")
def centiToInch():
    inch = input("Please enter a valid length in inches: ")
    centi = float(inch) * 2.54
    print ("length in centimeters: "+ str(centi) +" cm ")
centiToInch()
print ("--------------------------------------------")

# Problem 4
print ("--------------------------------------------")
print ("This is Problem 4: Slope\n")
print ("This program will sum a series of entered numbers")
def sum():
    num = int(input("How many numbers do you want summed?: "))
    input1 = num
    summation = 0
    while num > 0:
        num -= 1
        summation += float(input("Please input your " + str(input1 - num) + "st number: "))
    print ("The summation is: " + str(summation))
sum()
print ("--------------------------------------------")

# Problem 5
print ("--------------------------------------------")
print ("This is Problem 5: Fibonacci Sequence\n")
print ("This program will find the nth term of the fibonacci sequence")
term = int(input("Enter the nth term of fib sequence you want to find: "))
def nthfib(x):
    permterm = term
    if x == 1 or x == 2:
        print("Your " + str(x) +"th term is: 1")
    else:
        term1 = 1
        term2 = 1
        while x > 2:
            tempterm = term2
            term2 += term1
            term1 = tempterm
            x -= 1
        print("Your " + str(permterm) +"th fibonacci term is: " + str(term2))
nthfib(term)
print ("--------------------------------------------")