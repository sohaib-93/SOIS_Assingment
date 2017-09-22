#!/usr/bin/python3
'''Embedded Linux Assignment - Part B
Program 1: Using getopts, concept take input file(inp.txt) and output file(op.txt) as arguments and find
search for “Embedded” in inp.txt using regular expression and Implement the count in output file op.txt
'''


import re
import sys
import getopt


inputfile = ''
outputfile = ''
word = []
counter = 0

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["ifile=","ofile="])
except getopt.GetoptError:
    print('Error: test.py -i <inputfile> -o <outputfile>')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print('Command Line Format: test.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg

print('Input file is: ', inputfile)
print('Output file is: ', outputfile)

f1 = open(inputfile)
f2 = open(outputfile, "w")

text = f1.read()
wordsearch = len(re.findall('[Ee]mbedded\s', text))
print("The number of times the word \'Embedded\' is found in the text file is", wordsearch)
f2.write(str(wordsearch))

f1.close()
f2.close()
