# FrequencyArray Implementation

import sys

dnaFile = open("rosalind_data_p11.txt")
seq = dnaFile.readline()
k = dnaFile.readline()


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

frequency = [0] * (4**int(k))
for i in range(0,len(seq)-int(k)):
	kmer = seq[i:i+int(k)]
	ind = patternToNumber(kmer)
	frequency[ind] = frequency[ind] + 1

for i in frequency:
	print(i, end=" ")