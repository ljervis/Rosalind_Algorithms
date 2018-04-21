f = open("./data/rosalind_data_p39.txt", "r")

source = int(f.readline().strip())
sink = int(f.readline().strip())

graph = {}
for line in f:
    first, rest = line.strip().split("->")
    first = int(first)
    dest, cost = map(int, rest.split(":"))
    if first not in graph:
        graph[first] = {}
    graph[first][dest] = cost

def format_path(curr, sink, longest_path_choice):
    curr_node = curr
    answer = [curr_node]
    while curr_node != sink:
        curr_node = longest_path_choice[curr_node]
        answer.append(curr_node)
    return "->".join(map(str, answer))

def compute(curr_node, graph, source, sink, longest_path, longest_path_choice):
    if curr_node == sink:
        longest_path[sink] = 0
        return 0

    elif curr_node in longest_path:
        return longest_path[curr_node]
   
    else:

        longest_p = float('-inf')
        longest_p_c = None

        # if the current node has no children, it will never reach the sink.
        # return negative infinity.
        if curr_node not in graph:
            longest_path[curr_node] = float('-inf')
            longest_path_choice[curr_node] = None
            return float('-inf')

        for node in graph[curr_node]:
            res = graph[curr_node][node] + compute(node, graph, source, sink, longest_path, longest_path_choice)
            if res > longest_p:
                longest_p = res
                longest_p_c = node

        longest_path[curr_node] = longest_p
        longest_path_choice[curr_node] = longest_p_c
        return longest_p


longest_path = {}
longest_path_choice = {}
print (compute(source, graph, source, sink, longest_path, longest_path_choice))
print (format_path(source, sink, longest_path_choice))