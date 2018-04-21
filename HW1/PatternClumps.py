# PatternClumps Implementation

import sys


def symbolToNumber(symbol):
	if symbol == 'A':
		return 0
	elif symbol == 'C':
		return 1
	elif symbol == 'G':
		return 2
	elif symbol == 'T':
		return 3

def numberToSymbol(number):
	if number == 0:
		return 'A'
	elif number == 1:
		return 'C'
	elif number == 2:
		return 'G'
	elif number == 3:
		return 'T'

def patternToNumber(pattern):
	if pattern:
		symbol = pattern[len(pattern) - 1]
		prefix = pattern[:(len(pattern)-1)]
		return 4*patternToNumber(prefix)+symbolToNumber(symbol)
	else:
		return 0

def numberToPattern(index, k):
	if k == 1:
		return numberToSymbol(index)
	q, r = divmod(index, 4)
	symbol = numberToSymbol(r)
	prefixPattern = numberToPattern(q, k-1)
	return prefixPattern + symbol



dnaFile = open("rosalind_data_p5.txt")
seq = dnaFile.readline()
args = dnaFile.readline().split(" ")
k = int(args[0])
l = int(args[1])
t = int(args[2])
clumps = []


for i in range(0, len(seq) - l):
#	frequency = [0] * (k**4)
	freqDict = {}
	for j in range(i, i+l-k+1):
		kmer = seq[j:j+k]
		ind = patternToNumber(kmer)
		print(kmer + " " + str(ind))
		if str(ind) in freqDict:
			freqDict[str(ind)] = str(int(freqDict[str(ind)]) + 1)
		else:
			freqDict[str(ind)] = '1'
		if int(freqDict[str(ind)]) >= t and kmer not in clumps:
			clumps.append(kmer)
#		frequency[ind] = frequency[ind] + 1
#		if frequency[ind] >= t:
#			if kmer not in clumps:
#				clumps.append(kmer)

for i in clumps:
	print(i, end=" ")





