# LinearSpaceAlignment Implementation

import sys

def open_file(file_name):
    string_one = ""
    string_two = ""
    with open(file_name) as f:
        string_one = f.readline().rstrip("\n")
        string_two = f.readline().rstrip("\n")
    return (string_one, string_two)

def open_blosum(file_name):
    blosum_matrix = [[0]*21 for x in range(21)]
    ind = 0
    with open(file_name) as f:
        for line in f:
            line = line.rstrip("\n").split(" ")
            line[:] = [x for x in line if x != ""]
            blosum_matrix[ind] = line
            ind += 1
    return blosum_matrix

def blosum_score(i,j,direction,string_v,string_w,blosum_matrix):
    if direction == 0:
        string_v = string_v[::-1]
        string_w = string_w[::-1]
    blos_w = blosum_matrix[0].index(string_w[j-1])+1
    blos_v = blosum_matrix[0].index(string_v[i-1])+1
    return int(blosum_matrix[blos_v][blos_w])

def middle_column(n,m,direction,string_v,string_w,blosum_matrix):
    num_rows = 2
    indel_pen = 5   
    mid_ind = int(m/2) 
    score = [[0]*num_rows for x in range(n+1)]
    for x in range(1,n+1):
        score[x][0] = score[x-1][0]-indel_pen
    for y in range(1,num_rows):
        score[0][y] = score[0][y-1]-indel_pen
    for j in range(1,mid_ind+2):
        for i in range(1,n+1):
            score_curr = blosum_score(i,j,direction,string_v,string_w,blosum_matrix)
            col = 1
            score[i][col] = max(score[i-1][col-1]+score_curr,score[i-1][col]-indel_pen,score[i][col-1]-indel_pen)
        if j != mid_ind+1:
            score[0][0] = score[0][0]-indel_pen
            score[0][1] = score[0][1]-indel_pen
            for update in range(1,n+1):
                score[update][0] = score[update][1]
                score[update][1] = 0
    return score

def max_edge(from_source,from_sink,n,m):
    j = int(m/2)
    i = 0
    k = 0
    l = 0
    max_score_out = -10000000
    max_score_in = -100000000
    col_source = 0
    col_sink = 1
    if m%2 == 0:
            col_source = 0
            col_sink = 0
    for r in range(n+1):
        if from_source[r][col_source]+from_sink[n-r][col_sink] > max_score_out:
            i = r
            max_score_out = from_source[r][col_source]+from_sink[n-r][col_sink]
    if from_source[i+1][0]+from_sink[n-i+1][1] > max_score_in:
        k = i+1
        l = j
        max_score_in = from_source[n-i+1][0]+from_sink[i+1][1]
    if from_source[i][1]+from_sink[n-i][0] > max_score_in:
        k = i
        l = j+1
        max_score_in = from_source[n-i][0]+from_sink[i][1]
    if from_source[i+1][1]+from_sink[n-i+1][0] > max_score_in:
        k = i+1
        l = j+1
        max_score_in = from_source[i+1][1]+from_sink[n-i+1][0]
    return (i,j),(k,l)

def linear_space_alignment(top,bottom,left,right,align,string_v,string_w,blosum_matrix):
    if left == right:
        return align
    if bottom == top:
        return align
    middle = int(left+right/2)
    n, m = len(string_v[top:bottom+1]), len(string_w[left:right+1])
    from_source_column = middle_column(n,m,1,string_v[top:bottom],string_w[left:right],blosum_matrix)
    from_sink_column = middle_column(n,m,0,string_v[top:bottom],string_w[left:right],blosum_matrix)
    (i,j),(k,l) = max_edge(from_source_column,from_sink_column,n,m)
    middle_node = i
    linear_space_alignment(top,middle_node,left,middle,align,string_v[top:middle_node],string_w[left:middle],blosum_matrix)
    align.append(str(i)+str(j)+str(k)+str(l))
    if k == i+1 and l == j+1:
        middle += 1
        middle_node += 1
    if k == i and l == j+1:
        middle += 1
    if k == i+1 and l == j:
        middle_node += 1
    linear_space_alignment(middle_node,bottom,middle,right,align,string_v[middle_node:bottom],string_w[middle:right],blosum_matrix)

def main():
    (string_v,string_w) = open_file("./data/Rosalind_data_p47.txt")
    blosum_matrix = open_blosum("./data/blosum62.txt")
    n, m = len(string_v), len(string_w)
    align = [""]
    align = linear_space_alignment(0,n,0,m,align,string_v,string_w,blosum_matrix)
    print(align)

if __name__ == "__main__":
    main()