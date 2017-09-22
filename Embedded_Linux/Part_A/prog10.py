#!/usr/bin/python3
#Python Assignment
#Program 10: A) Create a dictionary of a) fruit name and its number B) Create a list from the dictionary for only orange and apple.

fruits = {"Mango":12, "Orange":54, "Apple":80, "Grapes":25, "Pears":15, "Banana":65}
fname = []

str1="Orange"
str2="Apple"

for key, value in fruits.items():
	if( str1 in key):
		org = [key, value]
		fname.append(org)
	elif( str2 in key):
		app = [key, value]
		fname.append(app)	

print ("The list containing Oranges and Apples", fname)
print ("The list containing only Apples", app)
print ("The list containing only Oranges", org)