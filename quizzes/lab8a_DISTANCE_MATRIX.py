from math import inf

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

graph_str = """\
D 2 W
0 1 4
"""

adj_list = adjacency_list(graph_str)
print(distance_matrix(adj_list))