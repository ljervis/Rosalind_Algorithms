#GraphToGenome Implementation

import sys

def open_file(file_name):
    graph_pairs = []
    with open(file_name) as f:
        graph_pairs = f.readline().rstrip("\n").split("),")
    for i in range(len(graph_pairs)):
        graph_pairs[i] = ''.join( c for c in graph_pairs[i] if  c not in '(,' )
        if i > 0:
            graph_pairs[i] = graph_pairs[i][1:]
    graph_pairs[len(graph_pairs)-1] = graph_pairs[len(graph_pairs)-1][:-1]
    return graph_pairs

def graph_to_genome(graph):
    num_blocks = len(graph)
    cycles = []
    cycle_num = 0
    cycles.append([])
    cycles[cycle_num].append(1)
    max_node = 0
    start_node = graph[j].split(" ")[0]
    for j in range(0, num_blocks):
        curr_node = graph[j].split(" ")
        for i in range(2):
            curr_num = int(curr_node[i])
            if curr_num == start_node and j > 0:
                cycles[cycle_num].append(start_node)
                cycle_num += 1
                start_node = max_node + 1
                cycles.append([])
            else:
                cycles[cycle_num].append(curr_num)
            if curr_num > max_node:
                max_node = curr_num
    if len(cycles) == 2:
        cycles[1].insert(0,cycles[1][len(cycles[1])-1])
    return cycles

def cycle_to_chromosome(cycle,start):
    n = len(cycle)
    s = start
    chromosome = list(range(start,int(n/2)+start))
    for x in range(len(chromosome)):
        chromosome[x] = "+"+str(chromosome[x])
    for j in range(0,n-1,2):
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
    graph = open_file("./data/rosalind_data_p58.txt")
    # print(graph)    
    cycles = graph_to_genome(graph)
    s = 1
    for i in range(len(cycles)):
        genome = cycle_to_chromosome(cycles[i],s)
        s = int((len(cycles[i])+1)/2)
        print_chromosome(genome)
    # genome = cycle_to_chromosome(cycles[0],1)
    # print_chromosome(genome)
    # genome = cycle_to_chromosome(cycles[1],int((len(cycles[0])+1)/2))
    # print_chromosome(genome)


if __name__ == "__main__":
    main()