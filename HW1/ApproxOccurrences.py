# ApproxOccurrences Implementation

import sys

dnaFile = open("rosalind_data_p8.txt")
pattern = dnaFile.readline().rstrip('\n')
seq = dnaFile.readline().rstrip('\n')
d = dnaFile.readline().rstrip('\n')

def hammingDistance(seq1, seq2):
	dist = 0
	for i in range(0, len(seq1)):
		if seq1[i] != seq2[i]:
			dist = dist + 1
	return dist


def approx(pattern, seq, d):
	ind = []
	for i in range(0, len(seq)-len(pattern)):
		seq1 = seq[i:i+len(pattern)]
		if (hammingDistance(seq1, pattern) <= int(d)):
			ind.append(i)
	return ind

output = approx(pattern, seq, d)

for i in output
		print(i, end=" ")
	