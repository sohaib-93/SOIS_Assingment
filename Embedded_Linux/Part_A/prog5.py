# !/usr/bin/python3
# Python Assignment
# Program 5: Implement a python code to get 5 username and password and store it in a dictionary.

import getpass

users = {}
user = []

for i in range(0,5):
	user = input("Enter the username: ")
	pswd = getpass.getpass("Enter the password: ")
	users[user] = pswd

print ("\n")

for key in users:
	print ('The user name:', key, 'and the password:', users[key])
