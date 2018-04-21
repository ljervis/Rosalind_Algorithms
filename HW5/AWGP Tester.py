# AWGP Tester
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

def score_function():
    gap_open = 11
    gap_extend = 1
    return gap_open, gap_extend

def initialize_matrices(lower, upper, n, m):
    min_value = -100
    for j in range(m+1):
        lower[0][j] = min_value
    for i in range(n+1):
        upper[i][0] = min_value

def fill_score_matrix(n,m, string_v, string_w, blosum_matrix):
    score_lower = [[0]*(m+1) for x in range(n+1)]
    score_upper = [[0]*(m+1) for x in range(n+1)]
    score_middle = [[0]*(m+1) for x in range(n+1)]
    initialize_matrices(score_lower, score_upper, n, m)
    gap_open, gap_extend = score_function()
    for j in range(m+1):
        for i in range(n+1):
            count = 0
            while count < 3:
                if count == 0:
                    if i != 0:
                        score_lower[i][j] = max(score_middle[i-1][j]-gap_open, score_lower[i-1][j]-gap_extend)
                    count += 1
                elif count == 1:
                    if j != 0:
                        score_upper[i][j] = max(score_middle[i][j-1]-gap_open, score_upper[i][j-1]-gap_extend)
                    count += 1
                else:
                    if i != 0 and j != 0:
                        blos_w = blosum_matrix[0].index(string_w[j-1])+1
                        blos_v = blosum_matrix[0].index(string_v[i-1])+1
                        score_curr = int(blosum_matrix[blos_v][blos_w])
                        score_middle[i][j] = max(score_middle[i-1][j-1]+score_curr, score_lower[i][j], score_upper[i][j])
                    count += 1
    alignment_v_final, alignment_w_final = back_track(score_lower, score_middle, score_upper, n, m, string_v, string_w, blosum_matrix)
    return score_middle[n][m], alignment_v_final, alignment_w_final

def back_track(lower, middle, upper, n, m, string_v, string_w, blosum_matrix):
    alignment_v = ""
    alignment_w = ""
    gap_open, gap_extend = score_function()
    i = n
    j = m
    level = 1
    while i != 0 and j != 0:
        if level == 0:
            if lower[i][j] == middle[i-1][j]-gap_open:
                level = 1
                alignment_v += string_v[i-1]
                alignment_w += "-"
                i += -1
            elif lower[i][j] == lower[i-1][j]-gap_extend:
                level = 0
                alignment_v += string_v[i-1]
                alignment_w += "-"
                i += -1
        elif level == 1:
            blos_w = blosum_matrix[0].index(string_w[j-1])+1
            blos_v = blosum_matrix[0].index(string_v[i-1])+1
            score_curr = int(blosum_matrix[blos_v][blos_w])
            if middle[i][j] == lower[i][j]:
                level = 0
            elif middle[i][j] == upper[i][j]:
                level = 2
            elif middle[i][j] == middle[i-1][j-1]+score_curr:
                level = 1
                alignment_v += string_v[i-1]
                alignment_w += string_w[j-1]
                i += -1
                j += -1
        else:
            if upper[i][j] == middle[i][j-1]-gap_open:
                level = 1
                alignment_v += "-"
                alignment_w += string_w[j-1]
                j += -1
            elif upper[i][j] == upper[i][j-1]-gap_extend:
                level = 2
                alignment_v += "-"
                alignment_w += string_w[j-1]
                j += -1
    return alignment_v[::-1], alignment_w[::-1]

        


def main():
    string_v, string_w = open_file("./data/Rosalind_data_p45.txt")
    string_v_len, string_w_len = len(string_v), len(string_w)
    blosum62 = open_blosum("./data/blosum62.txt")
    print("String v: " + string_v + "\nString w: " + string_w)
    max_length, alignment_v_final, alignment_w_final = fill_score_matrix(string_v_len,string_w_len,string_v,string_w,blosum62)
    print("max length: ")
    print(max_length)
    print(alignment_v_final)
    print(alignment_w_final)


if __name__ == "__main__":
    main()