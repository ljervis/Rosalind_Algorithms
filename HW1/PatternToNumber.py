# PatternToNumber Implementation

import sys

dnaFile = open("rosalind_data_p12.txt")
pattern = dnaFile.readline()

def symbolToNumber(symbol):
	if symbol == 'A':
		return 0
	elif symbol == 'C':
		return 1
	elif symbol == 'G':
		return 2
	elif symbol == 'T':
		return 3

def patternToNumber(pattern):
	if pattern:
		symbol = pattern[len(pattern) - 1]
		prefix = pattern[:(len(pattern)-1)]
		return 4*patternToNumber(prefix)+symbolToNumber(symbol)
	else:
		return 0

print(patternToNumber(pattern))