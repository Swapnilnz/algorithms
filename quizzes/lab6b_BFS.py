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


def bfs_tree(adj_list, start):
    n = len(adj_list)
    state = ['U' for i in range(n)]
    parent = [None for i in range(n)]
    queue = deque()
    state[start] = 'D'
    queue.append(start)
    return bfs_loop(adj_list, queue, state, parent)

def bfs_loop(adj_list, queue, state, parent):
    while len(queue) > 0:
        vert = queue.popleft()
        for tup in adj_list[vert]:
            edge = tup[0]
            if state[edge] == 'U':
                state[edge] = 'D'
                parent[edge] = vert
                queue.append(edge)
        state[vert] = 'P'
    return parent

# graph from the textbook example
graph_string = """\
D 2 W
0 1 99
"""

print(bfs_tree(adjacency_list(graph_string), 0))