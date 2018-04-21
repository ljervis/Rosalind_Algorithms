# SquaredErrorDistortion Implementation

import sys
from math import * 

def open_file(file_name):
    k = 0
    m = 0
    centers = []
    data_points = []
    with open(file_name) as f:
        k,m = f.readline().rstrip("\n").split(" ")
        for line in f:
            if line[0] == "-":
                break
            else:    
                centers.append(line.rstrip("\n").split(" "))
        for line in f:
            data_points.append(line.rstrip("\n").split(" "))
    for x in data_points:           #Convert data points to float
        for i,v in enumerate(x):
            x[i] = float(v)
    for x in centers:           #Convert data points to float
        for i,v in enumerate(x):
            x[i] = float(v)
    return int(k),int(m),data_points,centers

def min_distance(point,centers):
    min_dist = 100.0
    for c in centers:
        dist = euclidean_distance(c,point)
        if dist < min_dist:
            min_dist = dist
    return min_dist

def euclidean_distance(x,y): 
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def squared_error(data,centers):
    distance_squared = 0
    for d in data:
        distance_squared += pow(min_distance(d,centers),2)
    return distance_squared / len(data)

def main():
    k,m,data_points,centers = open_file("./data/rosalind_data_p76.txt")
    print(squared_error(data_points,centers))
    

if __name__ == "__main__":
    main()