# BWMatching Implementation

import sys

def open_file(file_name):
    text = ""
    patterns = {}
    with open(file_name) as f:
        text = f.readline().rstrip("\n")
        patterns = f.readline().rstrip("\n").split(" ")
    return text,patterns

def bwmatching(first_column, last_column, pattern, last_to_first):
    pat = pattern
    top = 0
    bottom = len(last_column)-1
    while top <= bottom:
        if pat:
            symbol = pat[-1]
            pat = pat[:-1]
            if last_column.count(symbol,top,bottom+1) > 0:
                top_index = last_column.find(symbol,top,bottom+1)
                bottom_index = last_column.rfind(symbol,top,bottom+1)
                top = last_to_first[top_index]
                bottom = last_to_first[bottom_index]
            else:
                return 0
        else:
            return bottom - top + 1

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

# Index in last_to_first corrosponds to index in last column for matching
def last_to_first_list(last_column,first_column):
    last_to_first = [0]*len(last_column)
    for index in range(len(last_column)):   
        occurence_number = find_occurence_number(last_column,index)
        nth_occurence_index = find_nth_ocurrence(first_column,last_column[index],occurence_number)
        last_to_first[index] = nth_occurence_index
    return last_to_first

def last_to_first_single(last_column, index):
    first_column = "".join(sorted(list(last_column)))
    occurence_number = find_occurence_number(last_column,index)
    nth_occurence_index = find_nth_ocurrence(first_column,last_column[index],occurence_number)
    return(nth_occurence_index)

if __name__ == "__main__":
    last_column, patterns = open_file("./data/rosalind_data_p73.txt")
    first_column = "".join(sorted(list(last_column)))
    last_to_first = last_to_first_list(last_column,first_column)    
    for pat in patterns:
        print(bwmatching(first_column,last_column,pat,last_to_first), end=" ")
    
