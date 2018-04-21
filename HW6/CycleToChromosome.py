#CycleToChromosome Implementation

import sys

def open_file(file_name):
    cycle = []
    with open(file_name) as f:
        cycle = f.readline().rstrip("\n").split(" ")
        cycle[0] = cycle[0][1:]
        cycle[len(cycle)-1] = cycle[len(cycle)-1][:-1]
    return cycle

def cycle_to_chromosome(cycle):
    n = len(cycle)
    chromosome = list(range(1,int(n/2)+1))
    for x in range(len(chromosome)):
        chromosome[x] = "+"+str(chromosome[x])
    for j in range(0,n,2):
        c = int(cycle[j+1])
        a = int(cycle[j])
        if c < a:
            chromosome[int(j/2)] = "-"+chromosome[int(j/2)][1:]
    return chromosome

def print_chromosome(chromosome):
    print("(",end="")
    print(" ".join(chromosome),end="")
    print(")")

def main():
    cycle = open_file("./data/rosalind_data_p56.txt")
    chromosome = cycle_to_chromosome(cycle)
    print_chromosome(chromosome)

if __name__ == "__main__":
    main()