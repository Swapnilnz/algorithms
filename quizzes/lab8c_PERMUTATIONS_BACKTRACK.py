def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        print(children(candidate, input_data))
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate, input_data):
    """Returns True if the candidate is complete solution"""
    return len(candidate) == len(input_data)

def children(candidate, input_data):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    new_c = []
    for element in input_data:
        if element not in candidate:
            new_c.append(candidate + (element,))
    return new_c

