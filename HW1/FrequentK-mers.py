# FrequentK-mers Implementation

import sys

dnaFile = open("rosalind_data_P2.txt")
seq = dnaFile.readline()
k = int(dnaFile.readline())
counts = []
counts.append(1)
maxCount = 0
for i in range(1,len(seq)-k):
	counts.append(0)
	for j in range(0,i):
		if seq[j:j+k] == seq[i:i+k]:
			counts[j] = counts[j] + 1
			if counts[j] > maxCount:
				maxCount = counts[j]
			break
		if j == i-1:
			counts[i] = counts[i] + 1

for ind, val in enumerate(counts):
	if val == maxCount:
		print(seq[ind:ind+k], end=" ")

