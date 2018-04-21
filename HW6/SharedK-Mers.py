# SharedK-Mers Implementation

import sys
import re

def read_file(file_name):
    k = 0
    string_one = ""
    string_two = ""
    with open(file_name) as f:
        k = int(f.readline().rstrip("\n"))
        string_one = f.readline().rstrip("\n")
        string_two = f.readline().rstrip("\n")
    # if len(string_one) != len(string_two):
    #     exit("input strings are not of equal length!")
    return k, string_one, string_two

def comp_kmer(kmer_one,kmer_two):
    if kmer_one == kmer_two:
        return 0
    else:
        return 1

def comp_rev_comp(kmer_one,kmer_two):
    # print(kmer_one+" "+kmer_two)
    k = len(kmer_two)
    kmer_two = kmer_two[::-1]
    # kmer_one = kmer_one[::-1]
    for i in range(k):
        if kmer_two[i] == "A":
            kmer_two = kmer_two[:i]+"T"+kmer_two[i+1:]
        elif kmer_two[i] == "T":
            kmer_two = kmer_two[:i]+"A"+kmer_two[i+1:]
        elif kmer_two[i] == "G":
            kmer_two = kmer_two[:i]+"C"+kmer_two[i+1:]
        elif kmer_two[i] == "C":
            kmer_two = kmer_two[:i]+"G"+kmer_two[i+1:]
        # if kmer_one[i] == "A":
        #     kmer_one = kmer_one[:i]+"T"+kmer_one[i+1:]
        # elif kmer_one[i] == "T":
        #     kmer_one = kmer_one[:i]+"A"+kmer_one[i+1:]
        # elif kmer_one[i] == "G":
        #     kmer_one = kmer_one[:i]+"C"+kmer_one[i+1:]
        # elif kmer_one[i] == "C":
        #     kmer_one = kmer_one[:i]+"G"+kmer_one[i+1:]
    # print(kmer_one+" "+kmer_two)
    return comp_kmer(kmer_one,kmer_two)

def rev_comp(kmer):
    k = len(kmer)
    kmer = kmer[::-1]
    # kmer_one = kmer_one[::-1]
    for i in range(k):
        if kmer[i] == "A":
            kmer = kmer[:i]+"T"+kmer[i+1:]
        elif kmer[i] == "T":
            kmer = kmer[:i]+"A"+kmer[i+1:]
        elif kmer[i] == "G":
            kmer = kmer[:i]+"C"+kmer[i+1:]
        elif kmer[i] == "C":
            kmer = kmer[:i]+"G"+kmer[i+1:]
    return kmer

def shared_kmers(k,string_one,string_two):
    n = len(string_one)
    kmer_pairs = []
    for i in range(n-k+1):
        for j in range(n-k+1):
            kmer_one = string_one[i:i+k]
            kmer_two = string_two[j:j+k]
            if comp_kmer(kmer_one,kmer_two) == 0 or comp_rev_comp(kmer_one,kmer_two) == 0:
                kmer_pairs.append((i,j))
    return kmer_pairs

def shared_kmers_alt(k,string_one,string_two):
    n = len(string_two)
    kmer_pairs = []
    for i in range(n-k+1):
        kmer_two = string_two[i:i+k]
        # is_in = string_one.find(kmer_two)
        is_in = [m.start() for m in re.finditer(kmer_two, string_one)]
        for j in is_in:
            kmer_pairs.append((j,i))
        kmer_two_comp = rev_comp(kmer_two)
        # is_in_comp = string_one.find(kmer_two_comp)
        is_in_comp = [m.start() for m in re.finditer(kmer_two_comp, string_one)]
        for j in is_in_comp:
            kmer_pairs.append((j,i))
    return kmer_pairs
        

def print_kmer_pairs(kmer_pairs):
    for i in kmer_pairs:
        print("("+str(i[0])+", "+str(i[1])+")")

def main():
    k, string_one, string_two = read_file("./data/rosalind_data_p54.txt")
    kmer_pairs = shared_kmers_alt(k,string_one,string_two)
    print_kmer_pairs(kmer_pairs)

if __name__ == "__main__":
    main()