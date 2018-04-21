# MultiplePatternMatching Implementation

import sys

def open_file(file_name):
    text = ""
    patterns = []
    with open(file_name) as f:
        text = f.readline().rstrip("\n")
        for line in f:
            patterns.append(line.rstrip("\n"))
    return text,patterns

def create_suffix_list(text):
    suffix_list = []
    ind = len(text) - 1
    for i in range(1,len(text)+1):
        suffix_list.append((text[-i:],ind))
        ind -= 1
    return suffix_list

def create_suffix_array(text):
    suffix_list = create_suffix_list(text)
    modified_suffix_list = []
    for suf in suffix_list:
        modified_suffix_list.append(suf[0][:-1])
    modified_suffix_list = sorted(modified_suffix_list)
    suffix_array = []
    for suf in modified_suffix_list:
        if suf == " ":
            suf = "$"
        else:
            suf += "$"
        for s in suffix_list:
            if s[0] == suf:
                suffix_array.append(s[1])
    return suffix_array

def count(symbol, i, column):
    c = 0
    for ind in range(i):
        if column[ind] == symbol:
            c += 1
    return c

def starting(suffix_array, bottom, top, patterns,text):
    starting_indices = []
    test_list = [2433,2460,92,93,94,96,95,926,927,928,929,930,931,932,933,943,944,945,955,967,968,969,970,971,972,973,974,997]
    while bottom - top > -1:
        if suffix_array[top] in test_list:
            print(text[suffix_array[top]:suffix_array[top]+len(patterns[0])])
            print(suffix_array[top])
            print(bottom)
            print(top)
        temp_pattern = text[suffix_array[top]:suffix_array[top]+len(patterns[0])]
        if temp_pattern in text and temp_pattern in patterns:
            starting_indices.append(suffix_array[top])
        top += 1
    return starting_indices

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
                return 0,0
        else:
            return bottom,top
                

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

def create_permutations(string):
    permutations = []
    for i in range(len(string)):
        ending = string[-i:]
        temp_string = ending + string[:-i]
        permutations.append(temp_string)
    return permutations

def bwt(permutations):
    bwt = ""
    length = len(permutations)
    permutations = sorted(permutations)
    for p in permutations:
        bwt += p[length-1]
    return bwt

def write_output(indices):
    with open("./output/rosalind_output_p76.txt","w") as f:
        for s in indices:
            f.write(str(s))
            f.write(" ")

def main():
    text, patterns = open_file("./data/MultiplePatternMatching.txt")
    text += "$"
    permutations = create_permutations(text)
    last_column = bwt(permutations)
    suffix_array = create_suffix_array(text)
    first_column = "".join(sorted(list(last_column)))
    first_occ = first_occurence(first_column) 
    last_to_first = last_to_first_list(last_column,first_column) 
    starting_indices = []
    for pat in patterns:
        bottom, top = bwmatching(first_column,last_column,pat,first_occ)
        if bottom + top != 0:
            starting_indices += starting(suffix_array,bottom,top, patterns, text)
    starting_indices = list(set(starting_indices))
    write_output(starting_indices)

if __name__ == "__main__":
    main()