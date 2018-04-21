#LongestRepeat Implementation 

import sys

def open_file(file_name):
    text = ""
    with open(file_name) as f:
        text = f.readline().rstrip("\n")
    return text

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

def create_suffix_tree(text):
    suffix_list = create_suffix_list(text)
    suffix_trie = create_trie(suffix_list)
    position = 0
    length = 0
    root = suffix_trie[0]

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


    # branches = [x[0] for x in branches]
    return branches

# def create_suffix_tree(trie, suffix_list):
#     branches = []
#     suffix_tree = {0:[" "]}
#     curr_node = 1
#     count = 0
#     for suf in suffix_list:
#         curr_node = 0
#         curr_branch = ""
#         count += 1
#         for s in suf:
#             if len(trie[curr_node]) > 1 and curr_node != 0:
#                 branches.append((curr_branch,curr_node))
#                 if curr_node not in suffix_tree:
#                     suffix_tree[curr_node] = []
#                 x = [x for x in suffix_tree[curr_node] if x[2] == curr_node]
#                 if not x: 
#                     suffix_tree[curr_node].append((curr_branch, len(suffix_list) - count, curr_node))
#                 v = [v for v in trie[curr_node] if v[1] == s]
#                 curr_node = v[0][0]
#                 curr_branch = ""
#             else:
#                 v = [v for v in trie[curr_node] if v[1] == s]
#                 curr_node = v[0][0]
#             curr_branch += s
#         branches.append((curr_branch,curr_node))
#         if curr_node not in suffix_tree:
#             suffix_tree[curr_node] = []
#         x = [x for x in suffix_tree[curr_node] if x[2] == curr_node]
#         if not x: 
#             suffix_tree[curr_node].append((curr_branch, len(suffix_list) - count, curr_node))
        
#     branches = list(set(branches))
#     branches = [x[0] for x in branches]
#     return suffix_tree


def longest_repeat(branches):
    candidates = []
    for v in branches:
        if v[len(v)-1] != "$":
            count = 0
            for b in branches:
                if v in b:
                    count += 1
            if count > 1:
                candidates.append(v)
    return max(candidates,key=len)


def output_function(branches):
    with open("./output/rosalind_output_p64.txt","w") as f:
        for b in branches:
            f.write(b+"\n")

def find_longest_repeat(suffix_tree,suffix_list,suffix_trie):
    longest_repeat_candidates = []
    for suf in suffix_list:
        curr_node = 0
        curr_branch = ""
        for s in suf:
            curr_branch += s
            if "$" not in suffix_tree[curr_node][0][0]:
                longest_repeat_candidates.append(curr_branch)
            curr_node += 1
    print(longest_repeat_candidates)


def main():
    text = open_file("./data/rosalind_data_p64.txt")
    suffix_list = create_suffix_list(text)
    suffix_trie = create_trie(suffix_list)
    branches = create_tree_branches(suffix_trie,suffix_list)
    # for b in branches:
    #     print(b)
    longest_branch = ""
    real_longest_branch = ""

    for b in branches:
        if b[4] == 1:
            ind = b[5].rfind(b[0])
            longest_branch = b[5][:ind+len(b[0])]
            if len(longest_branch) > len(real_longest_branch) and text.count(longest_branch) > 1:
                real_longest_branch = longest_branch
    print(real_longest_branch)

if __name__ == "__main__":
    main()