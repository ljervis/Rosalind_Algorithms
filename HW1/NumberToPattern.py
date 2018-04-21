# NumberToPattern Implementation

import sys

dnaFile = open("rosalind_data_p13.txt")
index = dnaFile.readline()
k = dnaFile.readline()

def numberToSymbol(number):
	if number == 0:
		return 'A'
	elif number == 1:
		return 'C'
	elif number == 2:
		return 'G'
	elif number == 3:
		return 'T'

def numberToPattern(index, k):
	if k == 1:
		return numberToSymbol(index)
	q, r = divmod(int(index), 4)
	symbol = numberToSymbol(r)
	prefixPattern = numberToPattern(q, int(k)-1)
	return prefixPattern + symbol

print(numberToPattern(index, k))	