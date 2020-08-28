
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


def dfs_backtrack(candidate, input_data, output_data, destination):
    if should_prune(candidate):
        return
    if is_solution(candidate, destination):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data, destination)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate_path, destination):
    """Returns True if the candidate is complete solution"""
    return candidate_path[-1] == destination

def children(candidate_path, adj_list):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    result = []
    last = candidate_path[-1]
    for vertex in adj_list[last]:
        if vertex[0] not in candidate_path:
            result.append(candidate_path + (vertex[0],))
    return result



def all_paths(adj_list, source, destination):
    solutions = []
    dfs_backtrack((source,), adj_list, solutions, destination)
    return solutions    

from pprint import pprint

# graph used in tracing bfs and dfs
graph_str = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""

adj_list = adjacency_list(graph_str)
pprint(sorted(all_paths(adj_list, 6, 3)))