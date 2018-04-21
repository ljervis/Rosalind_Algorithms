# ReverseComplement Implementation

import sys

newFile = open("rosalind_data_p3.txt")
seq = newFile.readline()

def RevComp(seq):
	complement = []
	for i in range(len(seq)-1,-1,-1):
		if seq[i] == 'A':
			complement.append('T')
		elif seq[i] == 'T':
			complement.append('A')
		elif seq[i] == 'G':
			complement.append('C')
		elif seq[i] == 'C':
			complement.append('G')
	return complement

output = RevComp(seq)

print("".join(output))
