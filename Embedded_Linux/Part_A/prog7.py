# !/usr/bin/python3
# Python Assignment
# Program 7: Implement a python code to find the centroid of a triangle.
# Formula to calculate the height of the tree, Height = tan(angle) * (Distance from the tree)

import math

adj = float(input("Please enter the distance from the tree: "))
ang = float(input("Please enter the angle(in radians): "))

height = (math.tan(ang) * adj)

print ("The height of the tree is", height)