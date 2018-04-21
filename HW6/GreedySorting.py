# GreedySorting Implementation

import sys

def open_file(file_name):
    permutation = []
    with open(file_name) as f:
        permutation = f.readline().rstrip("\n").split(" ")
        permutation[0] = permutation[0][1:]
        permutation[len(permutation)-1] = permutation[len(permutation)-1][:-1]
    return permutation

def greedy_sort(permutation):
    permutation_intermediates = []
    for ind in range(0,len(permutation)):
        permutation = invert(permutation, permutation_intermediates, ind)
    return permutation, permutation_intermediates

def invert(permutation,permutation_intermediates, index):
    if permutation[index][1:] != str(index+1):
        i = index+1
        p_i = permutation[index][1:]
        while p_i != str(index+1):
            p_i  = permutation[i][1:]
            i += 1
        inv_ind_str = index
        inv_ind_end = i-1
        while inv_ind_end - inv_ind_str > 0:
            permutation[inv_ind_str], permutation[inv_ind_end] = permutation[inv_ind_end], permutation[inv_ind_str]
            inv_ind_str, inv_ind_end = inv_ind_str+1, inv_ind_end-1
        for i in range(index,i):
            if permutation[i][0] == "+":
                permutation[i] = "-" + permutation[i][1:]
            elif permutation[i][0] == "-":
                permutation[i] = "+" + permutation[i][1:]
        permutation_intermediates.append("("+" ".join(permutation)+")")
        # print("(",end="")
        # print(" ".join(permutation),end="")
        # print(")")
    if permutation[index][1:] == str(index+1):
        if permutation[index][0] == "-":
            permutation[index] = "+" + permutation[index][1:]
            permutation_intermediates.append("("+" ".join(permutation)+")")
            # print("(",end="")
            # print(" ".join(permutation),end="")
            # print(")")
    return permutation

def write_to_file(permutation_intermediates, file_name):
    with open(file_name,"w") as f:
        for i in permutation_intermediates:
            f.write(i+"\n")

def main():
    starting_permutation = open_file("./data/rosalind_data_p50.txt")
    print("Starting Permutation:")
    print(starting_permutation)
    final_permutation, permutation_intermediates = greedy_sort(starting_permutation)
    print("Final Permutation:")
    print(final_permutation)
    write_to_file(permutation_intermediates,"./output/rosalind_output_p50.txt")
    

if __name__ == "__main__":
    main()