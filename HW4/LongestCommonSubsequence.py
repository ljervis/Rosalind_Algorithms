# LongestCommonSubsequence Implementation

import sys

def OpenFile(fileName):
    sequencePair = ()
    with open(fileName) as f:
        sequencePair = (f.readline().rstrip("\n"),f.readline().rstrip("\n"))
    return sequencePair


def createMatrices(dim):
    diagP, downP, rightP = 0,1,2
    score = [[0]*(dim[1]+1) for x in range(dim[0]+1)]
    back = [[0]*(dim[1]+1) for x in range(dim[0]+1)]
    down = [[0]*(dim[1]+1) for x in range(dim[0])]
    right = [[0]*dim[1] for x in range(dim[0]+1)]
    diag = [[0]*dim[1] for x in range(dim[0])]
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
    # print("Diag: ")
    # printHelper(diag, dim)
    diagP, downP, rightP = 0,1,2
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

def printHelper(matrix, dim):
    for x in range(dim[0]):
        for y in range(dim[1]):
            print(matrix[x][y],end="\t")
        print("")

def LongestCommonSubsequence(back, sequencePair):
    x = len(sequencePair[0])
    y = len(sequencePair[1])
    substring = ""
    while x != 0 and y != 0:
        if back[x][y] == 1:
            x += -1
        elif back[x][y] == 2:
            y += -1
        else:
            substring += sequencePair[0][x-1]
            x += -1
            y += -1
    return substring[::-1]


def main():
    sequencePair = OpenFile("./data/Rosalind_data_p38.txt")
    dim = (len(sequencePair[0]), len(sequencePair[1]))
    # print("Sequence Pairs:\n" + sequencePair[0] + "\n" + sequencePair[1])
    score, back = commonSubsequence(sequencePair)
    # print("Score Matrix: ")
    # printHelper(score, (dim[0]+1,dim[1]+1))
    # print("Back Pointer Matrix: ")
    # printHelper(back, (dim[0]+1,dim[1]+1))
    # print("Length of Common Subsequence: " + str(score[dim[0]][dim[1]]))
    subsequence = LongestCommonSubsequence(back, sequencePair)
    print("Longest Common Subsequence: ")
    print(subsequence)


main()




