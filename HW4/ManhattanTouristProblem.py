# ManhattanTouristProblem Implementation

import sys

def openFile(fileName):
    dim = (0,0)
    down = []
    right = []
    with open(fileName) as f:
        dimLine = f.readline().rstrip("\n").split(" ")
        dim = (int(dimLine[0]), int(dimLine[1]))
        down = [[0]*(dim[1]+1) for x in range(0,dim[0])]
        right = [[0]*(dim[1]) for x in range(0,dim[0]+1)]
        for x in range(0,dim[0]):
            dLine = f.readline().rstrip("\n").split(" ")
            for y in range(0,dim[1]+1):
                down[x][y] = int(dLine[y])
        f.readline()
        for x in range(0,dim[0]+1):
            rLine = f.readline().rstrip("\n").split(" ")
            for y in range(0,dim[1]):
                right[x][y] = int(rLine[y])
    return dim, down, right

dim, down, right = openFile("./data/Rosalind_data_p37.txt")


def traverseAlignmentGraph(down, right, dim):
    score = [[0]*(dim[1]+1) for x in range(0,dim[0]+1)]
    for n in range(1, dim[0]+1):
        score[n][0] = score[n-1][0]+down[n-1][0]
    for m in range(1, dim[1]+1):
        score[0][m] = score[0][m-1]+right[0][m-1]
    for n in range(1,dim[0]+1):
        for m in range(1,dim[1]+1):
            maxVals = [0]*2
            maxVals[0] = score[n-1][m] + down[n-1][m]
            maxVals[1] = score[n][m-1] + right[n][m-1]
            score[n][m] = max(maxVals)
    return score

print("down: ")
for i in range(dim[0]):
    for j in range(dim[1]+1):
        print(down[i][j], end=" ")
    print("")
print("right: ")
for i in range(dim[0]+1):
    for j in range(dim[1]):
        print(right[i][j], end=" ")
    print("")
score = traverseAlignmentGraph(down, right, dim)
# print("score: ")
# for i in range(5):
#     for j in range(5):
#         print(score[i][j], end=" ")
#     print("")
maxVal = score[dim[0]][dim[1]]
print("Longest Path: " + str(maxVal))