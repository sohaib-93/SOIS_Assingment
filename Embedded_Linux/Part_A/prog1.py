# !/usr/bin/python3
# Python Assignment
# Program 1: Implement a python code to find the hypotenuse of a right angle triangle.
# Formula for Pythagorus Theorem, (Hypotenuse^2) = (Altitude^2) + (Base^2)
# sqrt() has been import from math library to perform square root operation.

from math import sqrt

def pyth(alt,base):
	hyp = sqrt(alt**2 + base**2)
	return hyp

alt = float(input("Please enter the Altitude of the Right Triangle: "))
base = float(input("Please enter the Base of the Right Triangle: "))

print ("The Hypotenuse is:", pyth(alt,base))
