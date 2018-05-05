#FindAEularianPathInAGraph Implementation

import sys
import copy

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

def createCycle(adList):
    outgoingNode = ""
    incomingNode = ""
    num = 0
    noIncoming = 0
    for keyX, valX in adList.items():
        numOutgoing = len(valX)
        numIncoming = 0
        for keyY, valY in adList.items():
            for outEdge in valY:
                if outEdge == keyX:
                    numIncoming += 1
                if outEdge not in adList:
                    noIncoming = int(outEdge)
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
    if noIncoming != 0:
        outgoingNode = str(noIncoming)
        # print("outgoing node: "+str(outgoingNode))
        adList[outgoingNode] = []   
    adList[outgoingNode].append(incomingNode)
    return adList, incomingNode, outgoingNode

def eularianCycle(adList, keys, numEdges):
    # print(adList)
    adList, incomingNode, outgoingNode = createCycle(adList)
    numEdges += 1
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
    for i, v in enumerate(currCycle):
        if v == incomingNode and currCycle[i-1] == outgoingNode:
            incomingNodeInd = i
    currCycle = currCycle[incomingNodeInd:]+currCycle[0:incomingNodeInd]
    return currCycle
            
adList, keys, numEdges = openFile("Rosalind_data_p29.txt")
finalCycle = eularianCycle(adList,keys,numEdges)
with open("Rosalind_answer_p29.txt", "w") as f:
    for i in finalCycle[0:len(finalCycle)-1]:
        f.write(str(i) + "->")
    f.write(finalCycle[len(finalCycle)-1])
