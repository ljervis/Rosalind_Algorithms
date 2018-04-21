# InverseBurrowsWheelerTransform Implementation

import sys

def open_file(file_name):
    transform = []
    with open(file_name) as f:
        transform = f.readline().rstrip("\n")
    return transform

def find_nth_ocurrence(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

def find_occurence_number(haystack, index):
    needle = haystack[index]
    start = haystack.find(needle)
    n = 1
    while start != index:
        start = haystack.find(needle, start+1)
        n += 1
    return n

def invert_bwt(first_col, last_col):
    length = len(first_col)
    original_seq = ""
    curr_symbol = ("$",1)
    for i in range(length):
        temp_index = find_nth_ocurrence(last_col,curr_symbol[0],curr_symbol[1])
        curr_symbol = (first_col[temp_index],find_occurence_number(first_col,temp_index))
        original_seq += curr_symbol[0]
    return original_seq

def main():
    last_col = open_file("./data/rosalind_data_p70.txt")
    first_col = "".join(sorted(list(last_col)))
    original_seq = invert_bwt(first_col,last_col)
    print(original_seq)
    

if __name__ == "__main__":
    main()