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

def dfs_loop(adj_list, vert, states, parent, stack):
    for tup in adj_list[vert]:
        edge = tup[0]
        if states[edge] == 'U':
            states[edge] = 'D'
            parent[edge] = vert
            dfs_loop(adj_list, edge, states, parent, stack)
    states[vert] = 'P'
    stack.append(vert)
    
    

def starting_order(dependencies):
    adj_list = adjacency_list(dependencies)
    n = len(adj_list)
    states = ['U' for _ in range(n)]
    parent = [None for _ in range(n)]
    stack = []
    for i in range(n):
        if states[i] == 'U':
            dfs_loop(adj_list, i, states, parent, stack)
            
    stack.reverse()
    return stack

dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = starting_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))