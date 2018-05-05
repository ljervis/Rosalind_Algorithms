# DeBruijnGraphFromPathGraph Implementation

import sys 

def openFile(fileName):
    with open("Rosalind_data_p26.txt") as f:
        k = int(f.readline())
        text = f.readline()
    return k, text

def kMerComposition(text, k):
    composition = []
    for i in range(0, len(text)-k+1):
        composition.append(text[i:i+k])
    return composition

# def glueDuBruijnGraph(unGluedAdList):
    

def constructDeBruijnGraph(text, k):
    composition = kMerComposition(text, k-1)
    unGluedAdList = {}
    keys = []
    for ind, sPat in enumerate(composition):
        sufPat = sPat[1:]
        for pPat in composition[0:ind] + composition[ind+1:]:
            prefPat = pPat[0:len(pPat)-1]
            if sufPat == prefPat:
                if sPat not in unGluedAdList:
                    unGluedAdList[sPat] = []
                    keys.append(sPat)
                if pPat not in unGluedAdList[sPat]:
                    unGluedAdList[sPat].append(pPat)
    return unGluedAdList, keys

k, text = openFile("Rosalind_data_p26.txt")
unGluedAdList, keys = constructDeBruijnGraph(text, k)

with open("Rosalind_answer_p26.txt", "w") as w:
    for i in keys:
        w.write(i + " -> " + ",".join(str(x) for x in unGluedAdList[i]) + "\n")
   