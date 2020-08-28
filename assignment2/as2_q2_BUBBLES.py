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

def bfs_loop(adj_list, queue, state):
    connected = []
    while len(queue) > 0:
        vert = queue.popleft()
        for tup in adj_list[vert]:
            edge = tup[0]
            if state[edge] == 'U':
                state[edge] = 'D'
                connected.append(edge)
                queue.append(edge)
        state[vert] = 'P'
    return connected


def bubbles(physical_contact_info):
    adj_list = adjacency_list(physical_contact_info)
    n = len(adj_list)
    state = ['U' for _ in range(n)]
    queue = deque()
    components = []
    for i in range(n):
        if state[i] == 'U':
            prev_state = state
            state[i] = 'D'
            queue.append(i)
            connected = bfs_loop(adj_list, queue, state)
            components.append([i] + connected)
    return components

physical_contact_info = """\
U 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))