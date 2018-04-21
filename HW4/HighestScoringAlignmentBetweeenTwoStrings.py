# HighestScoringAlignmentBetweeenTwoStrings Implementation

import sys

def openFile(fileName):
    aaOne = ""
    aaTwo = ""
    with open(fileName) as f:
        aaOne = f.readline().rstrip("\n")
        aaTwo = f.readline().rstrip("\n")
    return (aaOne, aaTwo)

def openBLOSUM(fileName):
    blosum = [[0]*21 for x in range(21)]
    ind = 0
    with open(fileName) as f:
        for line in f:
            line = line.rstrip("\n").split(" ")
            line[:] = [x for x in line if x != ""]
            blosum[ind] = line
            # print(line)
            ind += 1
    return blosum

def printHelper(matrix, dim):
    for x in range(dim[0]):
        for y in range(dim[1]):
            print(matrix[x][y],end="\t")
        print("")

def createMatrices(dim):
    diagP, downP, rightP = 0,1,2
    score = [[0]*(dim[1]+1) for x in range(dim[0]+1)]
    back = [[0]*(dim[1]+1) for x in range(dim[0]+1)]
    down = [[-5]*(dim[1]+1) for x in range(dim[0])]
    right = [[-5]*dim[1] for x in range(dim[0]+1)]
    diag = [[0]*dim[1] for x in range(dim[0])]
    for x in range(1,dim[0]+1):
        back[x][0] = downP
    for y in range(1,dim[1]+1):
        back[0][y] = rightP
    return score, back, down, right, diag

def populateDiag(sequencePair, dim, diag, blosum62):
    for x in range(dim[0]):
        for y in range(dim[1]):
            seqX = sequencePair[0][x]
            blosX = blosum62[0].index(seqX)+1
            seqY = sequencePair[1][y]
            blosY = blosum62[0].index(seqY)+1
            diag[x][y] = int(blosum62[blosX][blosY])

def commonSubsequence(sequencePair, blosum62):
    dim = (len(sequencePair[0]), len(sequencePair[1]))
    score, back, down, right, diag = createMatrices(dim)
    populateDiag(sequencePair, dim, diag, blosum62)
    # print("Diag: ")
    # printHelper(diag, dim)
    diagP, downP, rightP = 0,1,2
    for x in range(1, dim[0]+1):
        score[x][0] = score[x-1][0] + down[x-1][0]
    for y in range(1, dim[1]+1):
        score[0][y] = score[0][y-1] + right[0][y-1]
    for x in range(1,dim[0]+1):
        for y in range(1,dim[1]+1):
            maxVal = [0]*3
            maxVal[0] = score[x-1][y] + down[x-1][y]
            maxVal[1] = score[x][y-1] + right[x][y-1]
            maxVal[2] = score[x-1][y-1] + diag[x-1][y-1]
            score[x][y] = max(maxVal)
            if score[x][y] == score[x-1][y] + down[x-1][y]:
                back[x][y] = downP
            elif score[x][y] == score[x][y-1] + right[x][y-1]:
                back[x][y] = rightP
            else:
                back[x][y] = diagP
    return score, back

def LongestCommonSubsequence(back, sequencePair):
    x = len(sequencePair[0])
    y = len(sequencePair[1])
    substringX = ""
    substringY = ""
    while x+y != 0:
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

def main():
    aaPair = openFile("./data/Rosalind_data_p40.txt")
    blosumMatrix = openBLOSUM("./data/BLOSUM62.txt")
    dim = (len(aaPair[0]), len(aaPair[1]))
    score, back = commonSubsequence(aaPair, blosumMatrix)
    # print("Score Matrix: ")
    # printHelper(score, (dim[0]+1,dim[1]+1))
    # print("Back Pointer Matrix: ")
    # printHelper(back, (dim[0]+1,dim[1]+1))
    # print("Length of Common Subsequence: " + str(score[dim[0]][dim[1]]))
    print(str(score[dim[0]][dim[1]]))
    alignmentX, alignmentY = LongestCommonSubsequence(back, aaPair)
    # print("Alignment: ")
    print(alignmentX)
    print(alignmentY)

main()