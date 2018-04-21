#ColoredEdges Implementation

import sys

def open_file(file_name):
    chromosomes = []
    with open(file_name) as f:
        chromosomes = f.readline().rstrip("\n").split(")(")
        chromosomes[0] = chromosomes[0][1:]
        chromosomes[len(chromosomes)-1] = chromosomes[len(chromosomes)-1][:-1]
    return chromosomes

def update_chromosomes(chromosomes):
    for i in range(len(chromosomes)):
        chromosomes[i] = chromosomes[i].split(" ")
        chromosomes[i].append(chromosomes[i][0])

def chromosome_to_cycle(chromosome):
    n = len(chromosome)
    nodes = [0]*(2*n)
    for j in range(1,len(chromosome)+1):
        i = chromosome[j-1]
        if i[0] == "+":
            nodes[2*j-2] = 2*int(i[1:])-1
            nodes[2*j-1] = 2*int(i[1:])
        else:
            nodes[2*j-2] = 2*int(i[1:])
            nodes[2*j-1] = 2*int(i[1:])-1
    return nodes

def colored_edges(chromosomes):
    edges = []
    for i in chromosomes:
        nodes = chromosome_to_cycle(i)
        for j in range(1,len(nodes)-1,2):
            edges.append((nodes[j],nodes[j+1]))
    return edges

def print_edges(edges):
    for i in range(len(edges)-1):
        print(edges[i],end=", ")
    print(edges[len(edges)-1])

def main():
    chromosomes = open_file("./data/rosalind_data_p57.txt")
    update_chromosomes(chromosomes)
    edges = colored_edges(chromosomes)
    print_edges(edges)

if __name__ == "__main__":
    main()