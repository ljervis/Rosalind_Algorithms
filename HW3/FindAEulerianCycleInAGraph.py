# FindAEularianCycleInAGraph Implementation

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


def eularianCycle(adList, keys, numEdges):
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
    return currCycle
            
adList, keys, numEdges = openFile("Rosalind_data_p28.txt")
finalCycle = eularianCycle(adList,keys,numEdges)
for i in finalCycle:
    print(i, end="->")
print(finalCycle[0])
        
    

