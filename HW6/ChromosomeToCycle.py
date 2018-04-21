#ChromosomeToCycle Implementation

import sys

def open_file(file_name):
    permutation = []
    with open(file_name) as f:
        permutation = f.readline().rstrip("\n").split(" ")
        permutation[0] = permutation[0][1:]
        permutation[len(permutation)-1] = permutation[len(permutation)-1][:-1]
    return permutation

def chromosome_to_cycle(permutation):
    n = len(permutation)
    nodes = [0]*(2*n)
    for j in range(1,len(permutation)+1):
        i = permutation[j-1]
        if i[0] == "+":
            nodes[2*j-2] = 2*int(i[1:])-1
            nodes[2*j-1] = 2*int(i[1:])
        else:
            nodes[2*j-2] = 2*int(i[1:])
            nodes[2*j-1] = 2*int(i[1:])-1
    return nodes

def print_nodes(nodes):
    for i in range(len(nodes)):
        nodes[i] = str(nodes[i])
    print("(",end="")
    print(" ".join(nodes),end="")
    print(")")

def main():
    permutation = open_file("./data/rosalind_data_p55.txt")
    nodes = chromosome_to_cycle(permutation)
    print_nodes(nodes)



if __name__ == "__main__":
    main()