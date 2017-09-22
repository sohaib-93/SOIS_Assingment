# !/usr/bin/python3
# Python Assignment
# Program 3: Implement a python code to find the distance between two points.(Euclidian distance)
# Formula for Euclidian distance, Distance = sqrt((x2-x1)^2 + (y2-y1)^2)

def edist(x1,y1,x2,y2):
	dist1 = (x2-x1)**2 + (y2-y1)**2
	dist = dist1**0.5
	return dist

x1 = float(input("Please enter the x co-ordinate of point 1: "))
y1 = float(input("Please enter the y co-ordinate of point 1: "))
x2 = float(input("Please enter the x co-ordinate of point 2: "))
y2 = float(input("Please enter the y co-ordinate of point 2: "))


#p1 and p2 contain x & y co-ordinates of Point 1 and Point 2 in the form of Tuples.
p1 = (x1,y1)  
p2 = (x2,y2)  

print ("The distance between Point 1", p1, "and Point 2", p2, " is:", edist(x1,y1,x2,y2))
