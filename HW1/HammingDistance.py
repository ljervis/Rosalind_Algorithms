# HammingDistance Implementation

import sys

dnaFile = open("rosalind_data_p7.txt")
seq1 = dnaFile.readline().rstrip('\n')
seq2 = dnaFile.readline().rstrip('\n')

hDist = 0

for i in range(0,len(seq1)):
	if seq1[i] != seq2[i]:
		hDist = hDist + 1

print(hDist)