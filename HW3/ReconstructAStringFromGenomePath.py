# ReconstructAStringFromGenomePath Implementation

import sys

newFile = open("Rosalind_data_p24.txt")
patterns = []
outputString = []
for line in newFile:
    patterns.append(line.rstrip("\n"))
k = len(patterns[0])
outputString += patterns[0][0:k]
for i in range(1, len(patterns)):
    outputString += patterns[i][k-1]
print("".join(outputString))