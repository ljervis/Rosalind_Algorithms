# BetterBWMatching Implementation

import sys

def open_file(file_name):
    text = ""
    patterns = {}
    with open(file_name) as f:
        text = f.readline().rstrip("\n")
        patterns = f.readline().rstrip("\n").split(" ")
    return text,patterns

def count(symbol, i, column):
    c = 0
    for ind in range(i):
        if column[ind] == symbol:
            c += 1
    return c


def bwmatching(first_column, last_column, pattern,first_occurence):
    pat = pattern
    top = 0
    bottom = len(last_column)-1
    while top <= bottom:
        if pat:
            symbol = pat[-1]
            pat = pat[:-1]
            if last_column.count(symbol,top,bottom+1) > 0:
                top = first_occurence[symbol] + count(symbol,top,last_column)
                bottom = first_occurence[symbol] + count(symbol,bottom+1,last_column)-1
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

def first_occurence(first_column):
    first_occ = {"$":0}
    curr_symbol = first_column[0]
    for ind in range(len(first_column)):
        if first_column[ind] != curr_symbol:
            curr_symbol = first_column[ind]
            first_occ[curr_symbol] = ind
    return first_occ
    
if __name__ == "__main__":
    last_column, patterns = open_file("./data/rosalind_data_p75.txt")
    first_column = "".join(sorted(list(last_column)))
    last_to_first = last_to_first_list(last_column,first_column)  
    first_occ = first_occurence(first_column) 
    for pat in patterns:
        print(bwmatching(first_column,last_column,pat,first_occ), end=" ")
    