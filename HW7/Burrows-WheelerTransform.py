#Burrows-WheelerTransform Implementation

import sys

def open_file(file_name):
    string = ""
    with open(file_name) as f:
        string = f.readline().rstrip("\n")
    return string

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
    
        
def main():
    string = open_file("./data/rosalind_data_p70.txt")
    permutations = create_permutations(string)
    transform = bwt(permutations)
    print(transform)

if __name__ == "__main__":
    main()
