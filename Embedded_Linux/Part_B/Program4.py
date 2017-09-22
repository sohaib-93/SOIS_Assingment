#!/usr/bin/python3
'''Embedded Linux Assignment - Part B
Program 4: Implement a lambda function for finding 
			a) square of number 
			b) area of triangle 
			c) area of circle
			d) area of a rectangle.
'''

num = int(input("Enter the number: "))
g = lambda x:x**2
print("The square of the number is :", g(num))

base = int(input("Enter the Base: "))
height = int(input("Enter the Height: "))
f = lambda x,y: 0.5*x*y
print("The area of the triangle is", f(base, height))

radius = int(input("Enter the radius: "))
j = lambda r: 3.14*r*r
print("The area of the circle is", j(radius))

length = int(input("Enter the Length: "))
breadth = int(input("Enter the Breadth: "))
k = lambda l1,b1: l1*b1
print("The area of the rectangle is", f(length, breadth))
