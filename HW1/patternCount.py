# PatternCount Implementation

import sys

dnaFile = open("rosalind_data_P1.txt")
seq = dnaFile.readline()
pattern = dnaFile.readline()
count = 0
for i in range(0,len(seq)-len(pattern)):
	if seq[i:i+len(pattern)] == pattern:
		count = count + 1
print(count)
