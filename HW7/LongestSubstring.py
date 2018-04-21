#LongestSubstring Implementation

import sys

def open_file(file_name):
    string_one = ""
    string_two = ""
    with open(file_name) as f:
        string_one = f.readline().rstrip("\n")
        string_two = f.readline().rstrip("\n")
    return string_one, string_two

def create_suffix_list(text):
    suffix_list = []
    ind = len(text) - 1
    for i in range(1,len(text)+1):
        suffix_list.append((text[-i:],ind))
        ind -= 1
    return suffix_list

def create_trie(patterns):
    trie_dict = {0:[]}
    curr_node = 0
    count = 1
    for pat in patterns:
        ind = pat[1]
        p = pat[0]
        for s in p:
            v = [v for v in trie_dict[curr_node] if v[1] == s]
            if v:
                curr_node = v[0][0]
                if v[0][2] > ind:
                   v[0] = (v[0][0],v[0][1],ind)
            else:
                trie_dict[curr_node].append((count,s,ind))
                curr_node = count
                trie_dict[count] = []
                count += 1
            ind += 1
        curr_node = 0
    return trie_dict

def create_tree_branches(trie, suffix_list):
    branches = []
    for suf in suffix_list:
        curr_node = 0
        curr_branch = ""
        position = suf[1]
        for s in suf[0]:
            if len(trie[curr_node]) > 1 and curr_node != 0:
                branches.append((curr_branch,curr_node,position,len(curr_branch), 1, suf[0]))
                v = [v for v in trie[curr_node] if v[1] == s]
                curr_node = v[0][0]
                position = v[0][2]                 
                curr_branch = ""
            else:
                v = [v for v in trie[curr_node] if v[1] == s]
                curr_node = v[0][0]               
            curr_branch += s
        branches.append((curr_branch,curr_node,position,len(curr_branch),0, suf[0]))
    for key,val in enumerate(branches):
        for k,v in enumerate(branches):
            if key != k and val[0] == v[0] and val[1] == v[1]:
                del branches[k]
    return branches

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n[0], visited)
    return visited

def main():
    string_one, string_two = open_file("./data/rosalind_data_p66.txt")
    # suffix_list_two = create_suffix_list(string_two)
    suffix_list_one = create_suffix_list(string_one)
    suffix_trie_one = create_trie(suffix_list_one)
    # suffix_trie_two = create_trie(suffix_list_two)

    max_sub = ""
    all_substrings = []
    for i in range(len(string_two)):
        for j in range(i):
            all_substrings.append(string_two[j:i])
    for sub in all_substrings:
        curr_node = 0
        count = 0
        for s in sub:
            count += 1
            v = [v for v in suffix_trie_one[curr_node] if v[1] == s]
            if v:
                curr_node = v[0][0]
                if count == len(sub):
                    if len(sub) > len(max_sub):
                        max_sub = sub
            else:
                break
    print(max_sub)

if __name__ == "__main__":
    main()