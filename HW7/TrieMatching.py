# TrieMatching Implementation

import sys

def open_file(file_name):
    text = ""
    patterns = []
    with open(file_name) as f:
        text = f.readline().rstrip("\n")
        for line in f:
            patterns.append(line.rstrip("\n"))
    return text, patterns

def prefix_trie_matching(pattern, trie):
    root = 0
    curr_node = root 
    leaf_pat = ""
    for symbol in pattern:
        v = [v for v in trie[curr_node] if v[1] == symbol]
        if v:
            curr_node = v[0][0]
            leaf_pat += symbol
            if not trie[curr_node]:
                return 0
        else:
            return 1

def trie_matching(text, trie):
    pattern_match_index = []
    for i in range(len(text)):
        prefix = text[i:]
        if prefix_trie_matching(prefix, trie) == 0:
            pattern_match_index.append(i)
    return pattern_match_index     

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

def create_ad_list(trie_dict):
    ad_list = []
    for key, val in trie_dict.items():
        for entry in val:
            ad_list.append(str(key) + "->" + str(entry[0]) + ":" + entry[1])
    return ad_list

def print_ind(inds):
    for ind in inds:
        print(str(ind),end=" ")

def main():
    text, patterns = open_file("./data/rosalind_data_p62.txt")
    trie = create_trie(patterns)
    pattern_match_index = trie_matching(text,trie)
    print_ind(pattern_match_index)
    
if __name__ == "__main__":
    main()