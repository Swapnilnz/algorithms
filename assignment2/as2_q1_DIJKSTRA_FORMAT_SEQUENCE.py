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
                result[ver1].append((ver2, 1))
                result[ver2].append((ver1, 1))                
        else:
            if 'W' in header:
                weight = edge[2]
                result[ver1].append((ver2, weight))
            else:
                result[ver1].append((ver2, 1))
                
    return result


def next_vertex(in_tree, distance):
    result_vert = None
    running_min = float('inf')
    for vertex in range(len(in_tree)):
        if in_tree[vertex]== False and distance[vertex] <= running_min:
            result_vert = vertex
            running_min = distance[vertex]
    
    return result_vert

def dijkstra(adj_list, start):
    num_ver = len(adj_list)
    in_tree = [False for _ in range(num_ver)]
    distance = [inf for _ in range(num_ver)]
    parent = [None for _ in range(num_ver)]
    distance[start] = 0
    while not all(in_tree):
        cur_vert = next_vertex(in_tree, distance)
        in_tree[cur_vert] = True
        for vertex, weight in adj_list[cur_vert]:
            if in_tree[vertex] == False and distance[cur_vert] + weight < distance[vertex]:
                distance[vertex] = distance[cur_vert] + weight
                parent[vertex] = cur_vert
    return (parent, distance)

def format_sequence(converters_info, source_format, destination_format):
    parent, distance = dijkstra(adjacency_list(converters_info), source_format)
    result = []
    if distance[destination_format] == inf:
        return "No solution!"
    else:
        running_index = destination_format
        while running_index != None:
            result.append(running_index)
            running_index = parent[running_index]
            
    result.reverse()
    return result
    
converters_info_str = """\
D 1
"""

print(format_sequence(converters_info_str, 0, 0))