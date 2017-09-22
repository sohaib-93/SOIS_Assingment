# !/usr/bin/python3
# Python Assignment
# Program 6: Implement a python code to find the centroid of a triangle.
# Formula for the centroid of the triangle, (x1+x2+x3/3 , y1+y2+y3/3)

x1 = float(input("Please enter the x co-ordinate of point 1: "))
y1 = float(input("Please enter the y co-ordinate of point 1: "))
x2 = float(input("Please enter the x co-ordinate of point 2: "))
y2 = float(input("Please enter the y co-ordinate of point 2: "))
x3 = float(input("Please enter the x co-ordinate of point 3: "))
y3 = float(input("Please enter the y co-ordinate of point 3: "))

centx = (x1+x2+x3)/3
centy = (y1+y2+y3)/3

cent = (centx, centy)

print ("The centroid of the circle is at", cent)
