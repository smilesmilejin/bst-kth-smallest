class TreeNode:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def inorder(current, values):
    if not current:
        return values
    
    inorder(current.left, values)
    values.append(current.key)
    inorder(current.right, values)

    return values

def kth_smallest(root, k):
    values = inorder(root, [])
    return values[k - 1]
