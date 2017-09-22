# !/usr/bin/python3
# Python Assignment
# Program 9: Implement a python code to count a) number of characters b) numbers of words c) number of lines from an input file to output file.

f = open("finput.txt", "r+")

text = f.read().splitlines()
lines = len(text)  # length of the list = number of lines
words = sum(len(line.split()) for line in text)  # split each line on spaces, sum up the lengths of the lists of words
characters = sum(len(line) for line in text)  # sum up the length of each line

print ("The number of line: ", lines)
print ("The number of word: ", words)
print ("The number of characters: ", characters)

f1 = open("foutput.txt", "w+")

f1.write("The number of line: "+str(lines)+"\n")
f1.write("The number of word: "+str(words)+"\n")
f1.write("The number of characters: "+str(characters))

f.close()
f1.close()