#!/usr/bin/python3
'''Embedded Linux Assignment - Part B
Program 2: Using argparse, concept take input file(inp.txt) and output file(op.txt) as arguments and find
search for “Embedded” in inp.txt using regular expression and Implement the count in output file op.txt
'''

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', action = 'store', dest = 'inputfile', help = 'Store a inputfile')
parser.add_argument('-o', action = 'store', dest = 'outputfile', help = 'Store a outputfile')

results = parser.parse_args()
print('inputfile =', results.inputfile)
print('outputfile =', results.outputfile)

f1 = open(results.inputfile)
f2 = open(results.outputfile, "w")

text = f1.read()
wordsearch = len(re.findall('[Ee]mbedded\s', text))
print("The number of times the word \'Embedded\' is found in the text file is", wordsearch)
f2.write(str(wordsearch))

f1.close()
f2.close()
