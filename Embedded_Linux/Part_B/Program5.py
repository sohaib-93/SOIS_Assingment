#!/usr/bin/python3
'''Embedded Linux Assignment - Part B
Program 5: Implement normal functions to find the numbers of words, lines, and characters in a file.
'''

def linecount(ifile):
	'''Function to count the number of line
	'''

	f = open(ifile, "r+")
	text = f.read().splitlines()
	lines = len(text)
	f.close();
	return lines


def wordcount(ifile):
	'''Function to count the number of words
	'''

	f = open(ifile, "r+")
	text = f.read().splitlines()
	lines = len(text)  
	words = sum(len(line.split()) for line in text)
	f.close();
	return words


def charcount(ifile):
	'''Function to count the number of characters
	'''

	f = open(ifile, "r+")
	text = f.read().splitlines()
	lines = len(text)
	words = sum(len(line.split()) for line in text)
	characters = sum(len(line) for line in text)
	f.close();
	return characters


ifile = input("Please enter the filename")

print("The number of line in the file are", linecount(ifile))
print("The number of words in the file are", wordcount(ifile))
print("The number of characters in the file are", charcount(ifile))

