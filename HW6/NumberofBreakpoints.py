#NumberOfBreakpoints Implementation

import sys

def open_file(file_name):
    permutation = []
    with open(file_name) as f:
        permutation = f.readline().rstrip("\n").split(" ")
        permutation[0] = permutation[0][1:]
        permutation[len(permutation)-1] = permutation[len(permutation)-1][:-1]
    return permutation

def add_boundary_blocks(permutaion):
    n = len(permutaion)
    permutaion.append("+"+str(n+1))
    permutaion.insert(0,"+0")

def number_breakpoints(permutation):
    num_breaks = 0
    n = len(permutation)
    for i in range(n-1):
        if permutation[i][0] == "-":
            one = int(permutation[i])
        else:
            one = int(permutation[i][1:])
        if permutation[i+1][0] == "-":
            two = int(permutation[i+1])
        else:
            two = int(permutation[i+1][1:])
        if two - one != 1:
            num_breaks += 1
            # print("Breakpoint:" + str(num_breaks))
            # print(one,end=",")
            # print(two)
    return num_breaks

def main():
    permutation = open_file("./data/rosalind_data_p51.txt")
    add_boundary_blocks(permutation)
    num_breaks = number_breakpoints(permutation)
    print(" ".join(permutation))
    print(num_breaks)


if __name__ == "__main__":
    main()

