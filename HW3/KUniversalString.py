# KUniversalString Implementation

import sys
import copy

def openFile(fileName):
    k = 0
    with open(fileName) as f:
        k = f.readline()
    return int(k[0])

def createKMers(k):
    k = int(k)
    if k == 1:
        kMers = ['0','1']
        return kMers
    kMers = createKMers(k-1)
    updatedKMers = [""]*len(kMers)*2
    count = 0
    for i in kMers:
        updatedKMers[count] = i+'1'
        updatedKMers[count+1] = i+'0'
        count += 2
    return updatedKMers

def compositionGraph(patterns):
    adList = {}
    keys = []
    numEdges = 0
    k = len(patterns[0])
    for pat in patterns:
        prefPat = pat[0:k-1]
        sufPat = pat[1:]
        if prefPat not in adList:
            adList[prefPat] = []
            keys.append(prefPat)
        adList[prefPat].append(sufPat)
        numEdges += 1        
    return adList, keys, numEdges


def createCycle(adList):
    outgoingNode = ""
    incomingNode = ""
    num = 0
    noIncoming = ""
    for keyX, valX in adList.items():
        numOutgoing = len(valX)
        numIncoming = 0
        for keyY, valY in adList.items():
            for outEdge in valY:
                if outEdge == keyX:
                    numIncoming += 1
                if outEdge not in adList:
                    noIncoming = outEdge
        if numOutgoing < numIncoming:
            num += 1
            outgoingNode = keyX
            # print("outgoing node: "+str(outgoingNode))
        elif numOutgoing > numIncoming:
            num += 1
            incomingNode = keyX
            # print("incoming node: "+str(incomingNode))
        if num > 2:
            print("More than two unbalenced nodes!")
    if noIncoming == "":
        edge = 0
        return adList, incomingNode, outgoingNode, edge
    if noIncoming != "":
        edge = 1
        outgoingNode = noIncoming
        # print("outgoing node: "+str(outgoingNode))
        adList[outgoingNode] = []   
    adList[outgoingNode].append(incomingNode)
    return adList, incomingNode, outgoingNode,edge

def eularianCycle(adList, keys, numEdges):
    # print(adList)
    adList, incomingNode, outgoingNode, edge = createCycle(adList)
    numEdges += edge
    # print(adList)
    incomingNodeInd = 0 
    currCycle = []
    currAdList = copy.deepcopy(adList)
    numEdges = int(numEdges)
    currNumEdges = 0
    currEdgeList = adList
    currEdge = adList[keys[0]][0]

    while currNumEdges < numEdges:
        if not currEdgeList[currEdge]:
            currCycle.append(currEdge)
            for i in currCycle:
                if currEdgeList[i]:
                    currEdge = i
                    break
            if not currEdgeList[currEdge]:
                return
            ind = currCycle.index(currEdge)
            currCycle = currCycle[ind:] + currCycle[1:ind]
        else:
            currCycle.append(currEdge)
            nextEdge = currEdgeList[currEdge][0]
            currEdgeList[currEdge] = currEdgeList[currEdge][1:]
            currNumEdges += 1
            currEdge = nextEdge
    if edge == 1:
        for i, v in enumerate(currCycle):
            if v == incomingNode and currCycle[i-1] == outgoingNode:
                incomingNodeInd = i
        currCycle = currCycle[incomingNodeInd:]+currCycle[0:incomingNodeInd]
    return currCycle

def cycleToString(cycle, k):
    k = int(k)
    diff = k - 2
    string = cycle[0]
    k = len(cycle[0])
    for i, v in enumerate(cycle[1:]):
        string += v[k-1]
    string = string[diff:]
    return string



k = openFile("Rosalind_data_p31.txt")
patterns = createKMers(k)
# print(patterns)
adList, keys, numEdges = compositionGraph(patterns) 
# print(numEdges)
# print(adList)
finalCycle = eularianCycle(adList,keys,numEdges)
# print(finalCycle)
finalString = cycleToString(finalCycle, k)

with open("Rosalind_answer_p31.txt", "w") as f:
    f.write(finalString)
    

