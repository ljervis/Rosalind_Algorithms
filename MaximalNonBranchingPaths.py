# MaximalNonBranchingPaths Implementation

import sys

def openFile(fileName):
    adList = {} 
    numEdges = 0
    keys = []
    with open(fileName) as f:
        for line in f:
            outNode = line.split(" ")[0]
            inNodes = line.rstrip("\n").split(" ")[2].split(",")
            adList[outNode] = inNodes
            keys.append(outNode)
            numEdges += len(inNodes)
    return adList, keys, numEdges

def isOneToOne(adList, keys, key):
    if key not in adList:
        return 0
    nodes = adList[key]
    if len(nodes) > 1:
        return 0
    numIncoming = 0    
    for k in keys:
        for n in adList[k]:
            if n == key:
                numIncoming += 1
    if numIncoming > 1 or numIncoming == 0:
        return 0
    return 1


def maxPaths(adList, keys):
    AllNonBranchingPaths = []
    AllIsolatedPaths = []
    for key in keys:
        if isOneToOne(adList, keys, key) == 0:
            for out in adList[key]:
                nonBranchingPath = key + " -> " + out
                branch = out
                while isOneToOne(adList, keys, branch) == 1:
                    nonBranchingPath += " -> " + adList[branch][0]
                    branch = adList[branch][0]
                AllNonBranchingPaths.append(nonBranchingPath)
        else:
            dup = 0
            for i in AllIsolatedPaths:
                if key in i:
                    dup = 1
            if dup == 0:
                branch = adList[key][0]
                isolatedBranch = key
                done = 0
                while isOneToOne(adList, keys, branch) == 1 and done == 0:
                    isolatedBranch += " -> " + branch                
                    if branch == key:
                        AllIsolatedPaths.append(isolatedBranch)
                        done = 1
                    else:
                        branch = adList[branch][0]
    return AllNonBranchingPaths + AllIsolatedPaths


adList, keys, numEdges = openFile("Rosalind_data_p35.txt")
paths = maxPaths(adList, keys)
for i in paths:
    print(i)