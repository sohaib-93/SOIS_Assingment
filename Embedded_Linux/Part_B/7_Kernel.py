#!/usr/bin/python3
'''Embedded Linux Assignment - Part B
Program 7: Implement a python code to download the stable version of kernel from kernel.org and delete it.
'''


import urllib.request
import os

#urllib is used to download the file from kernel.org
urllib.request.urlretrieve("https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.13.3.tar.xz", "linux-4.13.3.tar.xz")
print("The file has been downloaded")

os.remove("linux-4.13.3.tar.xz")
print("File has been removed!")
