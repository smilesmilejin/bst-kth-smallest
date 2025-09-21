class TreeNode:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def kth_smallest(root, k):
    """
    This function takes in the root of the tree and an integer k and returns the kth smallest value in the tree.
  
    Parameters:
    root (TreeNode): The root of the tree
    k (int): represents the kth smallest value which we would like to find
  
    Returns:
    int: the kth smallest value
    """
    values = []

    values_list = kth_smallest_helper(root, values)

    return values_list[k-1]

def kth_smallest_helper(current_node, values):
    if not current_node:
        return values
    
    # Inorder traversal (Left → Root → Right) -  gives sorted order by key.
    kth_smallest_helper(current_node.left, values)
    values.append(current_node.key)
    kth_smallest_helper(current_node.right, values)

    return values