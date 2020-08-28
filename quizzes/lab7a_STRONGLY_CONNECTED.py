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


def transpose(adj_list):
    transposed = [[] for _ in range(len(adj_list))]
    for vertex in range(len(adj_list)):
        for tup in adj_list[vertex]:
            vertex2 = tup[0]
            weight = tup[1]
            transposed[vertex2].append((vertex, weight))
    return transposed
    
    
def dfs_tree(adj_list, start):
    n = len(adj_list)
    states = ['U' for i in range(n)]
    parent = [None for i in range(n)]
    states[start] = 'D'
    states = dfs_loop(adj_list, start, states, parent)
    return states

def dfs_loop(adj_list, vert, states, parent):
    for tup in adj_list[vert]:
        edge = tup[0]
        if states[edge] == 'U':
            states[edge] = 'D'
            parent[edge] = vert
            dfs_loop(adj_list, edge, states, parent)
    states[vert] = 'P'
    
    return states

def is_strongly_connected(adj_list):
    vertex = 0
    states = dfs_tree(adj_list, vertex)
    stage1 = True
    for state in states:
        if state == 'U':
            stage1 = False
            
    stage2 = True
    if stage1:
        transposed = transpose(adj_list)
        transposed_states = dfs_tree(transposed, vertex)
        for state in transposed_states:
            if state == 'U':
                stage2 = False
                
    if stage1 and stage2:
        return True
    else:
        return False

graph_string = """\
D 3
0 1
1 0
0 2
"""

print(is_strongly_connected(adjacency_list(graph_string)))