#!/usr/bin/env python3

import time
from math import hypot

def euclidian_distance(city1,city2):
    return hypot(city1[0] - city2[0], city1[1] - city2[1])

def greedy_TSP(cities):
    total_d = 0 #distance travelled
    unvs = set(list(range(1,len(cities)))) #ids of cities not visited
    curr = 0
    
    while len(unvs)>0:
        min_d = float("inf")
        min_c = -1
        for c in unvs:
            d = euclidian_distance(cities[curr],cities[c])
            if (d < min_d):
                min_d = d
                min_c = c
        unvs.remove(min_c)
        total_d += min_d
        curr = min_c
    total_d += euclidian_distance(cities[curr],cities[0])
    return total_d

if __name__ == "__main__":
    file_name =  'GreedyTSPsimpletest.txt'

    start_time = time.time()

    with open(file_name, 'r') as f:
        nr_cities = int(f.readline().strip())
        cities = []
        
        for line in f:
            _, x, y = line.strip().split()
            cities.append((float(x), float(y)))

    print(greedy_TSP(cities))
    
    end_time = time.time()
    print(end_time - start_time)


