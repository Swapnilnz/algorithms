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


def next_vertex(in_tree, distance):
    result_vert = None
    running_min = float('inf')
    for vertex in range(len(in_tree)):
        if in_tree[vertex]== False and distance[vertex] <= running_min:
            result_vert = vertex
            running_min = distance[vertex]
    
    return result_vert

def prims(adj_list, start):
    n = len(adj_list)
    in_tree = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[start] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] == False and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
                
    return parent, distance

graph_string = """\
U 3 W
1 0 3
2 0 1
1 2 1
"""

print(prims(adjacency_list(graph_string), 1))
print(prims(adjacency_list(graph_string), 2))