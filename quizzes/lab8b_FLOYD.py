from math import inf
import copy

def adjacency_list(graph_str):
    raw = graph_str.splitlines()
    header = raw[0]
    n = int(header.split()[1])
    result = [[] for _ in range(n)]
    for edge in raw[1:]:
        edge = edge.split()
        for i in range(len(edge)):
            edge[i] = int(edge[i])
        ver1 = edge[0]
        ver2 = edge[1]
        if header[0] == 'U':
            if 'W' in header:
                weight = edge[2]
                result[ver1].append((ver2, weight))
                result[ver2].append((ver1, weight))
            else:
                result[ver1].append((ver2, None))
                result[ver2].append((ver1, None))                
        else:
            if 'W' in header:
                weight = edge[2]
                result[ver1].append((ver2, weight))
            else:
                result[ver1].append((ver2, None))
    return result

def distance_matrix(adj_list):
    num_v = len(adj_list)
    result = [[None for i in range(num_v)] for _ in range(len(adj_list))]
    temp_dic = {}
    for v1 in range(len(adj_list)):
        for v2, weight in adj_list[v1]:
            temp_dic[(v1, v2)] = weight
    for row in range(len(result)):
        for col in range(len(result[row])):
            if row == col:
                result[row][col] = 0
            elif (row, col) in temp_dic:
                result[row][col] = temp_dic[(row, col)]
            else:
                result[row][col] = inf
    return result

def floyd(distance):
    d_copy = copy.deepcopy(distance)
    n_rows = len(d_copy)
    for k in range(n_rows):
        for i in range(n_rows):
            for j in range(n_rows):
                if d_copy[i][j] > d_copy[i][k] + d_copy[k][j]:
                    d_copy[i][j] = d_copy[i][k] + d_copy[k][j]
    return d_copy


import pprint

graph_str = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""
d = [
[0,     5,   4,  inf],
[-4,    0,  -1,  inf],
[3,     8,   0,    4],
[inf, inf,   2,    0]
]
for i in (floyd(d)):
    print(i)