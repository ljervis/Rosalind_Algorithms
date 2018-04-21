# FittingAlignment Implementation

import sys

def openFile(fileName):
    stringOne = ""
    stringTwo = ""
    with open(fileName) as f:
        stringOne = f.readline().rstrip("\n")
        stringTwo = f.readline().rstrip("\n")
    return (stringOne, stringTwo)

def printHelper(matrix, dim):
    for x in range(dim[0]):
        for y in range(dim[1]):
            print(matrix[x][y],end="\t")
        print("")

def createMatrices(dim):
    diagP, downP, rightP = 0,1,2
    score = [[0]*(dim[1]+1) for x in range(dim[0]+1)]
    back = [[0]*(dim[1]+1) for x in range(dim[0]+1)]
    down = [[-1]*(dim[1]+1) for x in range(dim[0])]
    right = [[-1]*dim[1] for x in range(dim[0]+1)]
    diag = [[-1]*dim[1] for x in range(dim[0])]
    for x in range(1,dim[0]+1):
        back[x][0] = downP
    for y in range(1,dim[1]+1):
        back[0][y] = rightP
    return score, back, down, right, diag

def populateDiag(sequencePair, dim, diag):
    for x in range(dim[0]):
        for y in range(dim[1]):
            seqX = sequencePair[0]
            seqY = sequencePair[1]
            if seqX[x] == seqY[y]:
                diag[x][y] = 1

def commonSubsequence(sequencePair):
    dim = (len(sequencePair[0]), len(sequencePair[1]))
    score, back, down, right, diag = createMatrices(dim)
    populateDiag(sequencePair, dim, diag)
    # print("down: ")
    # printHelper(down, dim)
    diagP, downP, rightP = 0,1,2
    # for x in range(1, dim[0]+1):
    #     score[x][0] = score[x-1][0] - 1
    # for y in range(1, dim[1]+1):
    #     score[0][y] = score[0][y-1]- 1
    for x in range(1,dim[0]+1):
        for y in range(1,dim[1]+1):
            maxVal = [0]*3
            maxVal[0] = score[x-1][y] - 1
            maxVal[1] = score[x][y-1] - 1 
            maxVal[2] = score[x-1][y-1] + [-1,1][sequencePair[0][x-1] == sequencePair[1][y-1]]
            score[x][y] = max(maxVal)
            if score[x][y] == score[x-1][y] - 1:
                back[x][y] = downP
            elif score[x][y] == score[x][y-1] - 1:
                back[x][y] = rightP
            else:
                back[x][y] = diagP
    return score, back

def allSubstrings(seqY):
    substrings = []
    for i in range(0, len(seqY)):
        for j in range(1, len(seqY)+1):
            if seqY[i:j] != '' and seqY[i:j] not in substrings:
                substrings.append(seqY[i:j])
    return(substrings)

def LongestCommonSubsequence(back, sequencePair, coordinates):
    x = coordinates[0]
    y = coordinates[1]
    substringX = ""
    substringY = ""
    while x*y != 0:
        if back[x][y] == 1:
            substringX += sequencePair[0][x-1]
            substringY += "-"
            x += -1
        elif back[x][y] == 2:
            substringY += sequencePair[1][y-1]
            substringX += "-"
            y += -1
        else:
            substringX += sequencePair[0][x-1]
            substringY += sequencePair[1][y-1]
            x += -1
            y += -1
    return substringX[::-1], substringY[::-1]

def lengthOfSubstring(score, back, coordinates):
    x = coordinates[0]
    y = coordinates[1]
    length = 0
    while score[x][y] != 0:
        if back[x][y] == 1:
            x += -1
        elif back[x][y] == 2:
            y += -1
        else:
            x += -1
            y += -1
        length += 1
    return length

def maxScore(score, dim, back):
    scoreCoordinates = (0,0)
    maxLength = 0
    maxVal = 0
    for x in range(dim[0]+1):
        length = lengthOfSubstring(score, back, (x,dim[1]))
        val = score[x][dim[1]]
        if val >= maxVal and length >= maxLength:
            maxVal = val
            maxLength = length
            scoreCoordinates = (x,dim[1])
            
    # print(maxLength)
    return scoreCoordinates

def main():
    stringPair = openFile("./data/Rosalind_data_p43.txt")
    # seqYSubstrings = allSubstrings(stringPair[0])
    # for substring in seqYSubstrings:
    dim = (len(stringPair[0]), len(stringPair[1]))
    newStringPair = (stringPair[0], stringPair[1])
    score, back = commonSubsequence(newStringPair)
    # print("Score Matrix: ")
    # printHelper(score, (dim[0]+1,dim[1]+1))
    maxCoordinates = (0,0)
    maxS = 0
    for i in range(dim[0]+1):
        if score[i][dim[1]] > maxS:
            maxS = score[i][dim[1]]
            maxCoordinates = (i,dim[1])
    print(maxCoordinates)
    print(maxS)
    
    alignmentX, alignmentY = LongestCommonSubsequence(back, newStringPair, maxCoordinates)
    print(alignmentX)
    print(alignmentY)

main()