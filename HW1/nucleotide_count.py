# Counting DNA Nucleotides

import sys

dna_file = open("rosalind_dna.txt")
seq = dna_file.read()
count = [0,0,0,0] #[A,C,G,T]
for i in seq:
	if i == 'A':
		count[0] = count[0] + 1
	elif i == 'C':
		count[1] = count[1] + 1
	elif i == 'G':
		count[2] = count[2] + 1
	elif i == 'T':
		count[3] = count[3] + 1
print(count)
dna_file.close()