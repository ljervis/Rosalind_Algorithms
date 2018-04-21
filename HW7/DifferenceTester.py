#DifferenceTester

import sys

def open_file(file_name):
    branches = []
    with open(file_name) as f:
        for line in f:
            branches.append(line.rstrip("\n"))
    return branches


def compare_branches(correct,mine):
    for b in correct:
        if b not in mine:
            return 1
    return 0

def main():
    correct_branches = open_file("./output/rosalind_extra_data_output_p63.txt")
    my_branches = open_file("./output/rosalind_output_p63.txt")
    print(compare_branches(correct_branches,my_branches))



if __name__ == "__main__":
    main()