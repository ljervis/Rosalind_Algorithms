# MultipleGlobalAlignment Implementation

import sys

def openFile(fileName):
    aaOne = ""
    aaTwo = ""
    aaThree = ""
    with open(fileName) as f:
        aaOne = f.readline().rstrip("\n")
        aaTwo = f.readline().rstrip("\n")
        aaThree = f.readline().rstrip("\n")
    return aaOne, aaTwo, aaThree

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

def commonSubsequence(aaOne, aaTwo, aaThree):
    aaOneLen = len(aaOne)
    aaTwoLen = len(aaTwo)
    aaThreeLen = len(aaThree)
    score = [[[0]*(aaOneLen+1) for x in range(aaTwoLen+1)] for y in range(aaThreeLen+1)]
    for i in range(1,aaThreeLen+1):
        for j in range(1,aaTwoLen+1):
            for k in range(1,aaOneLen+1):
                s1 = score[i-1][j][k]
                s2 = score[i][j-1][k]
                s3 = score[i][j][k-1]
                s4 = score[i-1][j-1][k]
                s5 = score[i-1][j][k-1]
                s6 = score[i][j-1][k-1]
                currScore = 0
                if aaThree[i-1] == aaTwo[j-1] == aaOne[k-1]:
                    currScore = 1
                s7 = score[i-1][j-1][k-1] + currScore
                score[i][j][k] = max(s1,s2,s3,s4,s5,s6,s7)
    return score

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

def backtrack(score,aaOne,aaTwo,aaThree):
    i = len(aaThree)
    j = len(aaTwo)
    k = len(aaOne)
    stringOne = ""
    stringTwo = ""
    stringThree = ""
    while i != 0 and k!=0 and j!=0:
        currScore = 0
        if aaThree[i-1] == aaTwo[j-1] == aaOne[k-1]:
            currScore = 1
        if score[i][j][k] == score[i-1][j-1][k-1]+currScore:
            stringThree += aaThree[i-1]
            stringOne += aaOne[k-1]
            stringTwo += aaTwo[j-1]
            i += -1
            j += -1
            k += -1
        elif score[i][j][k] == score[i-1][j][k]:
            stringThree += aaThree[i-1]
            stringOne += "-"
            stringTwo += "-"
            i += -1
        elif score[i][j][k] == score[i-1][j-1][k]:
            stringThree += aaThree[i-1]
            stringOne += "-"
            stringTwo += aaTwo[j-1]
            i += -1
            j += -1
        elif score[i][j][k] == score[i][j-1][k]:
            stringThree += "-"
            stringOne += "-"
            stringTwo += aaTwo[j-1]
            j += -1
        elif score[i][j][k] == score[i][j][k-1]:
            stringThree += "-"
            stringOne += aaOne[k-1]
            stringTwo += "-"
            k += -1
        elif score[i][j][k] == score[i][j-1][k-1]:
            stringThree += "-"
            stringOne += aaOne[k-1]
            stringTwo += aaTwo[j-1]
            j += -1
            k += -1
        elif score[i][j][k] == score[i-1][j][k-1]:
            stringThree += aaThree[i-1]
            stringOne += aaOne[k-1]
            stringTwo += "-"
            i += -1
            k += -1
        elif score[i][j][k] == score[i-1][j-1][k-1]+currScore:
            stringThree += aaThree[i-1]
            stringOne += aaOne[k-1]
            stringTwo += aaTwo[j-1]
            i += -1
            j += -1
            k += -1
    while k != 0:
        stringOne += aaOne[k-1]
        k += -1
    while i != 0:
        stringThree += aaThree[i-1]
        i += -1
    while j != 0:
        stringTwo += aaTwo[j-1]
        j += -1
    maxLen = max(len(stringOne),len(stringTwo),len(stringThree))
    while len(stringOne) < maxLen:
        stringOne += "-"
    while len(stringTwo) < maxLen:
        stringTwo += "-"
    while len(stringThree) < maxLen:
        stringThree += "-"
    return stringOne[::-1],stringTwo[::-1],stringThree[::-1]
            


def main():
    aaOne,aaTwo,aaThree = openFile("./data/Rosalind_data_p48.txt")
    score = commonSubsequence(aaOne,aaTwo,aaThree)
    print(aaOne)
    print(aaTwo)
    print(aaThree)
    print(score[len(aaThree)][len(aaTwo)][len(aaOne)])
    stringOne, stringTwo, stringThree = backtrack(score,aaOne,aaTwo,aaThree)
    print(stringOne)
    print(stringTwo)
    print(stringThree)
    # print(score)
    

main()