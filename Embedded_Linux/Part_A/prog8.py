# !/usr/bin/python3
# Python Assignment
# Program 8: Implement a python code to solve quadratic equation.
# Quadratic Equation Formula: x = b^2 + (sqrt(b^2 - 4ac) / 2a) or b^2 - (sqrt(b^2 - 4ac) / 2a)

print ("ax^(2)+bx+c")
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

den = 2*a
brack1 = ((b*b) - (4*a*c))**0.5


num1 = -b + brack1 
num2 = -b - brack1

x1 = num1/den
x2 = num2/den

print ("The solution is", x1, ",", x2)
