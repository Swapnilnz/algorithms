import copy

def latin_squares(square):
    """Given a square (matrix) computes and returns Latin squares
    that can be obtained by replacing Nones with digits."""
    solutions = []
    dfs_backtrack(square, solutions)
    return solutions


def dfs_backtrack(candidate, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate):
            dfs_backtrack(child_candidate, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(copy.deepcopy(candidate))


def square_from_str(square_str):
    """Takes a string representation of a square and returns a matrix                                                                                                              
    (list of lists) representation where blanks are replaced with None."""
    return [[None if c == '-' else int(c) for c in line.strip()] for
            line in square_str.splitlines()]


def square_to_str(square):
    """Returns the string representation of the given square matrix."""
    return '\n'.join(''.join(str(c) for c in row) for row in square)

def should_prune(candidate):
    return False
    
    
def is_solution(candidate):
    
    for row in candidate:
        for col in row:
            if col == None:
                return False
    return True

def trans_helper(candidate):
    n = len(candidate)
    result = [[None for i in range(n)] for i in range(n)]
    for row in range(n):
        for col in range(n):
            result[col][row] = candidate[row][col]
    return result
            
def children(candidate):
    result = []
    n = len(candidate)    
    transposed_matrix = trans_helper(candidate)
    row = 0
    found = False
    while row < n and not found:
        col = 0
        
        while col < n and not found:
            if candidate[row][col] == None:
                found = True
                for num in range(n):
                    if num not in candidate[row] and num not in transposed_matrix[col]:
                        child = copy.deepcopy(candidate)
                        child[row][col] = num
                        result.append(child)
            col += 1
        row += 1
    return result

square = [[None]]
print(latin_squares(square))