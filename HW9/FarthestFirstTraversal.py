#FarthestFirstTraversal Implementation

import sys
from math import * 
import random

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
    for c in centers:
        dist = euclidean_distance(c,point)
        if dist < min_dist:
            min_dist = dist
    return min_dist

def populate_centers(data, centers, k):
    while k != 0:
        max_point = [0.0]*len(data[0])
        max_dist = 0.0
        for d in data:
            if d not in centers:
                dist = min_distance(d,centers)
                if dist > max_dist:
                    max_dist = dist
                    max_point = d
        centers.append(max_point)
        k -= 1


# def distance(data, centers, k):
#     while k != 0:
#         max_point = [0.0]*len(data[0])
#         max_dist = 0.0
#         for d in data:
#             if d not in centers:
#                 dist_sum = 0.0
#                 for c in centers:
#                     dist_sum += euclidean_distance(c,d)
#                 if dist_sum >= max_dist:
#                     max_dist = dist_sum
#                     max_point = d
#         centers.append(max_point)
#         k -= 1

def euclidean_distance(x,y): 
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def farthest_first_traversal(data, k):
    # centers = [data[random.randint(0,len(data)-1)]] #Passed Tests
    centers = [data[0]]
    k -= 1
    # print("center_test:")
    # print(centers)
    # print("float_test:")
    # print(centers[0][0] + centers[0][1])
    # distance(data,centers,k)
    populate_centers(data,centers,k)
    return centers

def main():
    k,m,data_points = open_file("./data/rosalind_data_p75.txt")
    centers = farthest_first_traversal(data_points,k)
    # print("data_points:")
    # print(data_points)
    # print("final_centers:")
    for c in centers:
        for i in c:
            print(i,end=" ")
        print()
    # test_calc()

def test_calc():
    one = [0.8,12.0,17.5,0.9,7.2]
    two = [0.3,16.4,8.90,34.6,24.6]
    c = [31.5,6.2,8.0,2.3,0.4] #my answer
    d = [32.3,1.9,5.1,16.2,8.8] #correct answer
    print(euclidean_distance(c,one))
    print(euclidean_distance(c,two))
    print(euclidean_distance(c,one)+euclidean_distance(c,two))
    print()
    print(euclidean_distance(d,one))
    print(euclidean_distance(d,two))
    print(euclidean_distance(d,one)+euclidean_distance(d,two))

if __name__ == "__main__":
    main()