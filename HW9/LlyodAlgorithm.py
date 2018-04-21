# LloydAlgorithm Implementation

import sys
from math import *

def open_file(file_name):
    k = 0
    m = 0
    data_points = []
    with open(file_name) as f:
        k,m = f.readline().rstrip("\n").split(" ")
        for line in f:
            data_points.append(line.rstrip("\n").split(" "))
    for x in data_points:           #Convert data points to float
        for i,v in enumerate(x):
            x[i] = float(v)
    return int(k),int(m),data_points


def min_distance(point,centers):
    min_dist = 100.0
    center = []
    for c in centers:
        dist = euclidean_distance(c,point)
        if dist < min_dist:
            min_dist = dist
            center = c
    return center

def euclidean_distance(x,y): 
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))


def centers_to_clusters(data,centers,m):
    for d in data:
        if len(d) == m:
            d.append([])
        temp_point = d[:-1]
        d[m] = min_distance(temp_point,centers)



# def clusters_to_centers(data,centers)


def llyods(data,k,m):
    centers = []
    for i in range(k):
        centers.append(data[i])
    print("centers:")
    print(centers)
    print("data_before:")
    print(data)
    centers_to_clusters(data,centers,m)
    print("data_after:")
    print(data)
    


def main():
    k,m,data_points = open_file("./data/rosalind_data_p77.txt")
    llyods(data_points,k,m)



if __name__ == "__main__":
    main()