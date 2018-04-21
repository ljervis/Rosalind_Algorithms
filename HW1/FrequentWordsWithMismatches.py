# FrequentWordsWithMismatches Implementation

import sys

dnaFile = open("rosalind_data_p9.txt")
seq = dnaFile.readline()
data = dnaFile.readline().split(" ")
k = data[0]
d = data[1]


def hammingDistance(seq1, seq2):
	dist = 0
	for i in range(0, len(seq1)):
		if seq1[i] != seq2[i]:
			dist = dist + 1
	return dist


def approxCount(pattern, seq, d):
	count = 0
	for i in range(0, len(seq)-len(pattern)):
		seq1 = seq[i:i+len(pattern)]
		if (hammingDistance(seq1, pattern) <= int(d)):
			count = count + 1
	return count

def neighbors(pattern, d):
	neighborhood = []
	if int(d) == 0:
		return pattern
	if len(pattern) == 1:
		return['A','T','G','C']
	patternSuffix = pattern[1:]
	suffix = neighbors(patternSuffix, int(d))
	for i in suffix:
		if hammingDistance(i, patternSuffix) < int(d):
			neighborhood.append('A'+i)
			neighborhood.append('G'+i)
			neighborhood.append('C'+i)
			neighborhood.append('T'+i)
		else:
			neighborhood.append(pattern[0]+i)
	return neighborhood

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

def freqWithMis(seq, k, d):
	close = [0] * (4**int(k))
	freqArr = [0] * (4**int(k))
	maxFreq = 0
	freqPatArr = []
	for i in range(0, len(seq)-int(k)):
		seq1 = seq[i:i+int(k)]
		n = neighbors(seq1, int(d))
		for x in n:
			ind = patternToNumber(x)
			close[ind] = 1
	for x in range(0, len(close)):
		if close[x] == 1:
			pat = numberToPattern(x, int(k))
			freqArr[x] = approxCount(pat, seq, int(d))
			if freqArr[x] > maxFreq:
				maxFreq = freqArr[x]
	for y in range(0, len(freqArr)):
		pat = numberToPattern(y, int(k))
		if freqArr[y] == maxFreq and pat not in freqPatArr:
			freqPatArr.append(pat)
	return freqPatArr

output = freqWithMis(seq, k, d)

for i in output:
	print(i, end=" ")



