# DAGTopologicalOrdering Implementation

import sys

def open_file(file_name):
    ad_list = {} 
    with open(file_name) as f:
        for line in f:
            out_node = line.split(" ")[0]
            in_nodes = line.rstrip("\n").split(" ")[2].split(",")
            ad_list[out_node] = in_nodes
    return ad_list

def has_incoming_edge(ad_list, node):
    has_incoming = 0
    for key,val in ad_list.items():
        if node != key:
            for outgoing_node in val:
                if outgoing_node == node:
                    has_incoming = 1
    return has_incoming

def incoming(ad_list, start_node, node):
    has_incoming = 0
    for key, val in ad_list.items():
        if node != start_node:
            for outgoing_node in val:
                if outgoing_node == node:
                    has_incoming = 1

def topological_order(ad_list):
    ordered_list = []
    candidate_nodes = []
    for node in ad_list:
        if has_incoming_edge(ad_list, node) == 0:
            candidate_nodes.append(node) 
    while candidate_nodes:
        start_node = candidate_nodes[0]
        if start_node not in ordered_list:
            ordered_list.append(start_node)
        candidate_nodes.pop(0)    
        if start_node in ad_list:
            for outgoing_edge in range(0,len(ad_list[start_node])):
                end_node = ad_list[start_node][0]
                ad_list[start_node] = ad_list[start_node][1:]
                if has_incoming_edge(ad_list, end_node) == 0:
                    candidate_nodes.append(end_node)
    return ordered_list

def main():
    ad_list = open_file("./data/Rosalind_data_p49.txt")
    print(ad_list)
    top_order = topological_order(ad_list)
    print(", ".join(top_order))


if __name__ == "__main__":
    main()