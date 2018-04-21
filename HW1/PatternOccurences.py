# PatternOccurences Implementation

import sys

newFile = open("rosalind_data_p4.txt")
pattern = newFile.readline().rstrip('\n')
seq = newFile.readline().rstrip('\n')
indices = []
for i in range(0,len(seq)-len(pattern)):
	if seq[i:i+len(pattern)] == pattern:
		indices.append(i)
for i in indices:
	print(i, end=" ")
