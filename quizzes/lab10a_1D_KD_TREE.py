# Do not alter the next two lines
from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

# Rewrite the following function to avoid slicing
def binary_search_tree(nums, is_sorted=False):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if not is_sorted:
        nums = sorted(nums)
    n = len(nums)
    if n == 1:
        tree = Node(nums[0], None, None)  # A leaf
    else:
        mid = n // 2  # Halfway (approx)
        left = binary_search_tree(nums[:mid], True)
        right = binary_search_tree(nums[mid:], True)
        tree = Node(nums[mid - 1], left, right)
    return tree

def binary_search_tree(nums, is_sorted=False, start_index=0, end_index=None, first=True):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if first:
        end_index = len(nums) - 1
    if not is_sorted:
        nums = sorted(nums)
    n = end_index - start_index + 1
    if n == 1: # base case
        tree = Node(nums[start_index], None, None)
    else:
        mid = n // 2 + start_index # halfway or lowest
        left = binary_search_tree(nums, True, start_index, mid - 1, False)
        right = binary_search_tree(nums, True, mid, end_index, False)
        tree = Node(nums[mid - 1], left, right)
    return tree


# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)
        
 
 


nums = [228]
tree = binary_search_tree(nums)
print_tree(tree)