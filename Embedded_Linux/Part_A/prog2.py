# !/usr/bin/python3
# Python Assignment
# Program 2: Implement a python code to find the area of a triangle.

def areat(alt,base):
	return (alt*base*0.5)
	
alt = float(input("Please enter the Altitude of the Triangle: "))
base = float(input("Please enter the Base of the Triangle: "))

print ("The area of triangle is:", areat(alt,base))
