# FirstToLastMapping Implementation

import sys

def open_file(file_name):
    last_column = ""
    index = 0
    with open(file_name) as f:
        last_column = f.readline().rstrip("\n")
        index = int(f.readline().rstrip("\n"))
    return last_column, index

def find_occurence_number(haystack, index):
    needle = haystack[index]
    start = haystack.find(needle)
    n = 1
    while start != index:
        start = haystack.find(needle, start+1)
        n += 1
    return n

def find_nth_ocurrence(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

def last_to_first(last_column, index):
    first_column = "".join(sorted(list(last_column)))
    occurence_number = find_occurence_number(last_column,index)
    nth_occurence_index = find_nth_ocurrence(first_column,last_column[index],occurence_number)
    return(nth_occurence_index)

def main():
    last_column, index = open_file("./data/rosalind_data_p71.txt")
    print(last_to_first(last_column,index))


if __name__ == "__main__":
    main()

