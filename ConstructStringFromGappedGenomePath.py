# ConstructStringFromGappedGenomePath Implementaion

import sys
import copy

def openFile(fileName):
    readPairs = []
    with open(fileName) as f:
        args = f.readline().rstrip("\n").split(" ")
        k, d = int(args[0]),int(args[1])
        for line in f:
            readOne = line[0:k]
            readTwo = line[k+1:].rstrip("\n")
            readPairs.append((readOne, readTwo))
    return k, d, readPairs

def splitPairs(readPairs):
    firstPatterns = []
    secondPatterns = []
    for first, second in readPairs:
        firstPatterns.append(first)
        secondPatterns.append(second)
    return firstPatterns, secondPatterns

def constructString(patterns, k):
    k = int(k)
    string = patterns[0]
    for pat in patterns[1:]:
        string += pat[k-1]
    return string

def combineStrings(firstString, secondString, k, d):
    d = int(d)
    k = int(k)
    combinedString = firstString + secondString[-(k+d):]
    return combinedString


k, d, readPairs = openFile("Rosalind_data_p34.txt")
firstPatterns, secondPatterns = splitPairs(readPairs)
firstString = constructString(firstPatterns, k)
secondString = constructString(secondPatterns, k)
combinedString = combineStrings(firstString, secondString, k, d)

# print(firstString)
# print(secondString)
print(combinedString)

