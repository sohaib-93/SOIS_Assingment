# !/usr/bin/python3
# Python Assignment
# Program 4: Implement a python code to get the username and password.

import getpass

user = input("Enter the username: ")
pswd = getpass.getpass("Enter the password: ")

print ('The name is', user, "and the password is", pswd)
