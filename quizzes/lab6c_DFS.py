from collections import deque

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

def dfs_tree(adj_list, start):
    n = len(adj_list)
    state = ['U' for i in range(n)]
    parent = [None for i in range(n)]
    state[start] = 'D'
    parent = dfs_loop(adj_list, start, state, parent)
    return parent

def dfs_loop(adj_list, vert, state, parent):
    for tup in adj_list[vert]:
        edge = tup[0]
        if state[edge] == 'U':
            state[edge] = 'D'
            parent[edge] = vert
            dfs_loop(adj_list, edge, state, parent)
    state[vert] = 'P'
    
    
    return parent


gstring = """\
D 4
0 3
"""
al = adjacency_list(gstring)
#for vert in al:
    
print(dfs_tree(adjacency_list(gstring), 0))