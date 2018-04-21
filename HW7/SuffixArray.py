#SuffixArray Implementation

import sys

def open_file(file_name):
    string_one = ""
    with open(file_name) as f:
        string_one = f.readline().rstrip("\n")
    return string_one

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

def main():
    string = open_file("./data/rosalind_data_p68.txt")
    suffix_list = create_suffix_list(string)
    modified_suffix_list = []
    suffix_array = []
    for suf in suffix_list:
        modified_suffix_list.append(suf[0][:-1])
    modified_suffix_list = sorted(modified_suffix_list)
    for suf in modified_suffix_list:
        if suf == " ":
            suf = "$"
        else:
            suf += "$"
        for s in suffix_list:
            if s[0] == suf:
                suffix_array.append(s[1])
    for s in range(len(suffix_array)):
        if s == len(suffix_array)-1:
            print(suffix_array[s])
        else:
            print(suffix_array[s],end=", ")
    
    # suffix_trie = create_trie(suffix_list)
    # branches = create_tree_branches(suffix_trie,suffix_list)
    # print(suffix_list)
    

if __name__ == "__main__":
    main()