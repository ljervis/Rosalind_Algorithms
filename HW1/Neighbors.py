# Neighboors Implementation

import sys

dnaFile = open("rosalind_data_p14.txt")
seq = dnaFile.readline().rstrip('\n')
d = dnaFile.readline().rstrip('\n')

def immediateNeighbors(pattern):
	imNeighbors = [pattern]
	for i in range(0, len(pattern)):
		if pattern[i] != 'A':
			imNeighbors.append(pattern[0:i]+'A'+pattern[i+1:])
		if pattern[i] != 'T':
			imNeighbors.append(pattern[0:i]+'T'+pattern[i+1:])
		if pattern[i] != 'G':
			imNeighbors.append(pattern[0:i]+'G'+pattern[i+1:])
		if pattern[i] != 'C':
			imNeighbors.append(pattern[0:i]+'C'+pattern[i+1:])
	return imNeighbors

def hammingDistance(seq1, seq2):
	dist = 0
	for i in range(0, len(seq1)):
		if seq1[i] != seq2[i]:
			dist = dist + 1
	return dist

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


output = neighbors(seq, d)

outputFile = open("p14_output.txt", "w")
for i in output:
	outputFile.write(i)
	outputFile.write("\n")