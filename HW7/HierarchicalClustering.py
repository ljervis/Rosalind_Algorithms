# HierarchicalClustering Implementation

import sys

def open_file(file_name):
    n = 0
    count = 0
    with open(file_name) as f:
        n = int(f.readline().rstrip("\n"))
        distance_matrix = {}
        for line in f:
            line_list = line.rstrip("\n").split(" ")
            distance_matrix[count] = {}
            for i in range(count,len(line_list)-1):
                distance_matrix[count][i+1] = float(line_list[i+1])
            count += 1
    return n, distance_matrix


def find_min(distance_matrix):
    min_val = sys.maxsize
    min_centers = ()
    for r_k,r_v in distance_matrix.items():
            for c_k,c_v in r_v.items():
                if c_v < min_val:
                    min_val = c_v
                    min_centers = (r_k,c_k)
    return min_centers


def hierarchical_clustering(n,distance_matrix,clusters):
    cluster_num = n
    k = n
    while cluster_num > 1:
        cluster_num -= 1
        min_centers = find_min(distance_matrix)
        distance_matrix[k] = {}
        for r in distance_matrix:
            if r != k:
                dist = 0
                if min_centers[0] in distance_matrix[r]:
                    dist += distance_matrix[r][min_centers[0]]*len(clusters[min_centers[0]])
                if r in distance_matrix[min_centers[0]]:
                    dist += distance_matrix[min_centers[0]][r]*len(clusters[min_centers[0]])
                if min_centers[1] in distance_matrix[r]:
                    dist += distance_matrix[r][min_centers[1]]*len(clusters[min_centers[1]])
                if r in distance_matrix[min_centers[1]]:
                    dist += distance_matrix[min_centers[1]][r]*len(clusters[min_centers[1]])
                s = len(clusters[min_centers[0]])+len(clusters[min_centers[1]])
                clusters[k] = list(clusters[min_centers[0]]+clusters[min_centers[1]])
                distance_matrix[k][r] = float(dist)/s
        k += 1
        for r in distance_matrix:
            if min_centers[0] in distance_matrix[r]:
                distance_matrix[r].pop(min_centers[0])
            if min_centers[1] in distance_matrix[r]:
                distance_matrix[r].pop(min_centers[1])
        distance_matrix.pop(min_centers[0])
        distance_matrix.pop(min_centers[1])
    return clusters
        
def print_clusters(clusters,n):
    count = 0
    for c_k,c_v in clusters.items():
        count += 1
        if count > n:
            for k in c_v:
                print(k+1,end=" ")
            print()

def main():
    n, distance_matrix = open_file("./data/rosalind_data_p79.txt")
    clusters = {}
    for i in range(n):
        clusters[i] = [i]
    clusters = hierarchical_clustering(n,distance_matrix,clusters)
    print_clusters(clusters,n)

if __name__ == "__main__":
    main()
