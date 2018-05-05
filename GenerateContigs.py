# GenerateContigs Implementation

import sys
import copy

def openFile(fileName):
    patterns = []
    with open(fileName) as f:
        for line in f:
            patterns.append(line.rstrip("\n"))
    return patterns

def compositionGraph(patterns):
    adList = {}
    nodeList = []
    k = len(patterns[0])
    count = 0
    for pat in patterns:
        prefPat = pat[0:k-1]
        sufPat = pat[1:]
        if prefPat not in adList:
            adList[prefPat] = []
            adList[prefPat].append(str(count))
            count += 1
        adList[prefPat].append(sufPat)
        if sufPat not in nodeList:
            nodeList.append(sufPat)
        if prefPat not in nodeList:
            nodeList.append(prefPat)
            
    return adList, nodeList

def isOneToOne(adList, key):
    if key not in adList:
        return 0
    nodes = adList[key]
    if len(nodes) > 2:
        return 0
    numIncoming = 0    
    for k, v in adList.items():
        for n in adList[k][1:]:
            if n == key:
                numIncoming += 1
    if numIncoming > 1 or numIncoming == 0:
        return 0
    return 1

def generateContigs(adList, nodeList):
    contigs = []
    for node in nodeList:
        if node in adList:
            contig = node 
            nodeOutEdges = adList[node][1:]
            for ind, out in enumerate(nodeOutEdges):
                currContig = contig + out[len(out)-1]
                curr = out
                if curr in adList and adList[curr][0] != adList[node][0]:

                    while curr in adList and isOneToOne(adList, curr) == 1:
                        temp = curr
                        curr = adList[curr][1]
                        currContig += curr[len(curr)-1]     
                        if adList[temp][0] == adList[node][0]:
                            nodeList.pop(nodeList.index(temp))
                            break               
                contigs.append(currContig)
    # for ind, val in enumerate(contigs):
    #     for cont in contigs:
    #         if val in cont and len(cont) > len(val):
    #             contigs.pop(ind)
    minCont = []
    ind = 0
    for cont in contigs:
        for val in contigs:
            if val in cont[1:] and val not in minCont:
                minCont.append(val)
    # print(minCont)
    for i in minCont:
        contigs = [x for x in contigs if x != i]
    return contigs
            
    

patterns = openFile("Rosalind_data_p33.txt")
adList, nodeList = compositionGraph(patterns)
# print(adList)
# print(nodeList)
allContigs = generateContigs(adList, nodeList)

with open("Rosalind_answer_p33.txt","w") as f:
    for i in allContigs:
        f.write(i + " ")
