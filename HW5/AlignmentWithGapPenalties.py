# AlignmentWithGapPenalties Implementation

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
            # print(line)
            ind += 1
    return blosum_matrix

def fill_upper_dag(n,m,ad_list):
    ending_index = (n+1)*(m+1)-(n+1)
    for x in range(ending_index):
        ad_list[x].append(x+n+1)
        ad_list[x].append(x+(2*n)+2)
    for x in range(ending_index,ending_index+(n+1)):
        ad_list[x].append(x+(2*n)+2)

def fill_middle_dag(n,m,ad_list):
    starting_index = (n+1)*(m+1)
    ending_index = starting_index + ((n+1)*(m+1)-(n+2))
    for x in range(starting_index, ending_index):
        ad_list[x].append(x+n+2)
    for x in range(starting_index, ending_index+1):
        ad_list[x].append(x-n-1)
    count = 0
    for x in range(starting_index, ending_index+n+1):
        if n-count != 0:
            ad_list[x].append(x+(n+1)*(m+1)+1)
        else:
            count = -1
        count += 1


def fill_lower_dag(n,m,ad_list):
    starting_index = 2*(n+1)*(m+1)
    ending_index = starting_index + ((n+1)*(m+1)-1)
    count = 0
    for x in range(starting_index, ending_index):
        if n-count != 0:
            ad_list[x].append(x+1)
        else:
            count = -1
        count += 1
    for x in range(starting_index, ending_index+1):
        ad_list[x].append(x-((n+1)*(m+1)))
    
def create_penalty_dag(n,m):
    dag_ad_list = [[x] for x in range(3*(n+1)*(m+1))]
    fill_upper_dag(n,m,dag_ad_list)
    fill_middle_dag(n,m,dag_ad_list)
    fill_lower_dag(n,m,dag_ad_list)
    return dag_ad_list

def topological_order(n,m):
    number_of_nodes = 3*(n+1)*(m+1)
    top_order = [0]*number_of_nodes
    count = 0
    for x in range((n+1)*(m+1)):
        top_order[count] = 2*(n+1)*(m+1)+x
        count += 1
        top_order[count] = x
        count += 1
        top_order[count] = (n+1)*(m+1)+x
        count += 1
    return top_order[2:]

def score_function():
    gap_open = -11
    gap_extend = 1
    return gap_open, gap_extend

def fill_score_matrix(n,m,top_order, string_v, string_w, blosum_matrix):
    score_lower = [[0]*(m+1) for x in range(n+1)]
    score_upper = [[0]*(m+1) for x in range(n+1)]
    score_middle = [[0]*(m+1) for x in range(n+1)]
    gap_open, gap_extend = score_function()
    count = 0
    for j in range(m):
        for i in range(n):
            if i == 0 or j == 0:
                continue
            elif count == 0:
                score_lower[i][j] = max(score_middle[i-1][j]-gap_open, score_lower[i-1][j]-gap_extend)
                count += 1
            elif count == 1:
                score_upper[i][j] = max(score_middle[i][j-1]-gap_open, score_upper[i][j-1]-gap_extend)
                count += 1
            else:
                blos_w = blosum_matrix[0].index(string_w[i])+1
                blos_v = blosum_matrix[0].index(string_v[j])+1
                score_curr = int(blosum_matrix[blos_v][blos_w])
                score_middle[i][j] = max(score_middle[i-1][j-1]+score_curr, score_lower[i][j], score_upper[i][j])
                count = 0
    return max(score_lower[n][m], score_middle[n][m], score_upper[n][m])
        


def main():
    string_v, string_w = open_file("./data/Rosalind_data_p45.txt")
    string_v_len, string_w_len = len(string_v), len(string_w)
    blosum62 = open_blosum("./data/blosum62.txt")
    print("String v: " + string_v + "\nString w: " + string_w)
    penalty_dag = create_penalty_dag(string_v_len, string_w_len)
    top_order = topological_order(string_v_len, string_w_len)
    print("topological order of nodes in DAG: ")
    print(top_order)
    max_length = fill_score_matrix(string_v_len,string_w_len,top_order,string_v,string_w,blosum62)
    print(max_length)


if __name__ == "__main__":
    main()
    