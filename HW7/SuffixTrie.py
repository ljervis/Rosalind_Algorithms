#SuffixTrie Implementation

import sys
import itertools

def open_file(file_name):
    text = ""
    with open(file_name) as f:
        text = f.readline().rstrip("\n")
    return text

def create_suffix_list(text):
    suffix_list = []
    for i in range(1,len(text)+1):
        suffix_list.append(text[-i:])
    return suffix_list

def create_trie(patterns):
    trie_dict = {0:[]}
    curr_node = 0
    count = 1
    for pat in patterns:
        for s in pat:
            v = [v for v in trie_dict[curr_node] if v[1] == s]
            if v:
               curr_node = v[0][0]
            else:
                trie_dict[curr_node].append((count,s))
                curr_node = count
                trie_dict[count] = []
                count += 1
        curr_node = 0
    return trie_dict

def create_tree_branches(trie, suffix_list):
    branches = []
    for suf in suffix_list:
        curr_node = 0
        curr_branch = ""
        for s in suf:
            if len(trie[curr_node]) > 1 and curr_node != 0:
                branches.append((curr_branch,curr_node))
                v = [v for v in trie[curr_node] if v[1] == s]
                curr_node = v[0][0]
                curr_branch = ""
            else:
                v = [v for v in trie[curr_node] if v[1] == s]
                curr_node = v[0][0]
            curr_branch += s
        branches.append((curr_branch,curr_node))
    branches = list(set(branches))
    branches = [x[0] for x in branches]
    return branches

def print_function(branches):
    for b in branches:
        print(b)

def output_function(branches):
    with open("./output/rosalind_output_p63.txt","w") as f:
        for b in branches:
            f.write(b+"\n")

def main():
    text = open_file("./data/rosalind_data_p63.txt")
    suffix_list = create_suffix_list(text)
    suffix_trie = create_trie(suffix_list)
    branches = create_tree_branches(suffix_trie,suffix_list)
    branches.sort(key=len)
    output_function(branches)

if __name__ == "__main__":
    main()