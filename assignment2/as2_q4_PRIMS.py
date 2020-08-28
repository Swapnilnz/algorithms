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

def prim(adj_list):
    n = len(adj_list)
    in_tree = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[0] = 0
    while not all(in_tree):
        vertex1 = next_vertex(in_tree, distance)
        in_tree[vertex1] = True
        for vertex2, weight in adj_list[vertex1]:
            if (not in_tree[vertex2]) and (weight < distance[vertex2]):
                distance[vertex2] = weight
                parent[vertex2] = vertex1
                
    return parent

def which_walkways(campus_map):
    adj_list = adjacency_list(campus_map)
    parent = prim(adj_list)
    result = []
    for v in range(len(parent)):
        if parent[v] != None:
            result.append(tuple(sorted((parent[v], v))))
            
    result = sorted(result)
    return result

	
	
campus_map = """\
U 1 W
"""

print(sorted(which_walkways(campus_map)))
