#!/usr/bin/python3
'''Embedded Linux Assignment - Part B
Program 6: Implement a python code to find the kernel version.
'''


import platform

print("The Kernel version is",platform.uname()[2])