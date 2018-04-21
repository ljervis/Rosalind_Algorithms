# LongestPathInADAG Implementation

import sys
import copy

def openFile(fileName):
    ssNodes = (0,0)
    adList = {}
    keys = []
    with open(fileName) as f:
        ssNodes = (f.readline().rstrip("\n"), f.readline().rstrip("\n"))
        for line in f:
            weightNodePair = (line[line.index(">")+1:line.index(":")], line[line.index(":")+1:line.index("\n")])
            if line[0:line.index("->")] not in adList:
                adList[line[0:line.index("->")]] = []
            adList[line[0:line.index("->")]].append(weightNodePair)
            keys.append(line[0:line.index("->")])
    return ssNodes, adList, keys

def hasIncomingEdge(adList, node):
    hasIncoming = 0
    for key,val in adList.items():
        if node != key:
            for outgoingNode in val:
                if outgoingNode[0] == node:
                    hasIncoming = 1
    return hasIncoming

def findIncomingEdgeNodes(adList, node):
    incomingNodes = []
    for key,val in adList.items():
        if node != key:
            for outgoingNode in val:
                if outgoingNode[0] == node and outgoingNode[1] != "-100":
                    incomingNodes.append(key)
    return incomingNodes

def removeSourceNodes(adList, ssNodes, keys, order):
    for node in order:
        if node != ssNodes[0]:
            if hasIncomingEdge(adList, node) == 0:
                if node in adList:
                    adList.pop(node)
                    keys.pop(keys.index(node))
                order.pop(order.index(node))

def topologicalOrder(adList, keys):
    orderedList = []
    candidateNodes = []
    for node in keys:
        if hasIncomingEdge(adList, node) == 0:
            candidateNodes.append(node) 
    while candidateNodes:
        startNode = candidateNodes[0]
        if startNode not in orderedList:
            orderedList.append(startNode)
        candidateNodes.pop(0)    
        if startNode in adList:
            for outgoingEdge in range(0,len(adList[startNode])):
                endNode = adList[startNode][0]
                adList[startNode] = adList[startNode][1:]
                if hasIncomingEdge(adList, endNode[0]) == 0:
                    candidateNodes.append(endNode[0])
    return orderedList

def longestPath(adList, order, ssNodes):
    length = 0
    path = ""
    score = {}
    startingNode = order[0]
    score[startingNode] = ("na","0")
    maxNode = ""
    for i in range(1,len(order)):
        currNode = order[i]
        incomingNodes = findIncomingEdgeNodes(adList, currNode)
        maxEdge = 0
        for n in incomingNodes:
            node = adList[n]
            for edge in node:
                if edge[0] == currNode:
                    if int(edge[1]) > maxEdge:
                        maxEdge = int(edge[1])
                        maxNode = n
        if maxNode != "":
            score[currNode] = (maxNode, str(int(score[maxNode][1])+maxEdge))
        else:
            score[currNode] = ("na", "-100")
    return score
    
def tracePath(ssNodes, score):
    path = []
    path.append(ssNodes[1])
    currNode = ssNodes[1]
    while currNode != ssNodes[0] and currNode != "na":
        path.append(score[currNode][0])
        currNode = score[currNode][0]
    return path[::-1]

def main():
    ssNodes, adList, keys = openFile("./data/Rosalind_data_p39.txt")
    print(adList)
    adListCopy = copy.deepcopy(adList)
    topOrder = topologicalOrder(adListCopy, keys)
    print(topOrder)
    # removeSourceNodes(adList,ssNodes,keys,topOrder)
    # print(adList)
    score = longestPath(adList, topOrder, ssNodes)
    # print(score)
    print(score[ssNodes[1]][1])
    path = tracePath(ssNodes, score)
    finalPath = ""
    for i in path:
        finalPath += i
        finalPath += "->"
    finalPath = finalPath[:-2]
    print(finalPath)
    

main()
    