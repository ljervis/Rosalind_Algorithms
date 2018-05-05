# DeBruijnGraphFromKMers Implementation

import sys 

def openFile(filename):
    with open(filename) as f:
        patterns = []
        for line in f:
            patterns.append(line.strip("\n"))
    return patterns

def compositionGraph(patterns):
    adList = {}
    keys = []
    k = len(patterns[0])
    for pat in patterns:
        prefPat = pat[0:k-1]
        sufPat = pat[1:]
        if prefPat not in adList:
            adList[prefPat] = []
            keys.append(prefPat)
        adList[prefPat].append(sufPat)
    return adList, keys

patterns = openFile("Rosalind_data_p27.txt")
adList, keys = compositionGraph(patterns)


with open("Rosalind_answer_p27.txt", "w") as w:
    for i in keys:
        w.write(i + " -> " + ",".join(str(x) for x in adList[i]) + "\n")