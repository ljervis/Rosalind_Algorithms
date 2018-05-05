#OverlapGraphProblem Implementation

import sys

newFile = open("Rosalind_data_p25.txt")
patterns = []
for line in newFile:
    patterns.append(line.rstrip("\n"))
adjacencyList = []
for ind, sPat in enumerate(patterns):
    sufPat = sPat[1:]
    for pPat in patterns[0:ind] + patterns[ind+1:]:
        prefPat = pPat[0:len(pPat)-1]
        if sufPat == prefPat:
            adjacencyList.append(sPat + " -> " + pPat)
print("\n".join(adjacencyList))