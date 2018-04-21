# MinSkew Implementation

import sys

dnaFile = open('rosalind_data_p6.txt')
seq = dnaFile.readline()

ind = []
ind.append(0)
diff = 0
minVal = 0
for i in range(0, len(seq)):
	if seq[i] == 'G':
		diff = diff+1
	elif seq[i] == 'C':
		diff = diff-1
	ind.append(diff)
	if diff < minVal:
		minVal = diff

minVals = []
for i in range(0, len(ind)):
	if ind[i] == minVal:
		minVals.append(i)

for i in minVals:
	print(i, end =" ")
