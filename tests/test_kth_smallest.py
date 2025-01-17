from activity.main import TreeNode, kth_smallest
import pytest

def test_kth_smallest_on_valid_bst():
    #Arrange 
    root = TreeNode(6, TreeNode(3, TreeNode(1), TreeNode(5)),TreeNode(8, None, TreeNode(9)))
    k = 3

    #Act
    result = kth_smallest(root, k)
    #Assert
    assert result == 5

def test_kth_smallest_with_less_balanced_bst():
    #Arrange
    root = TreeNode(5, TreeNode(3, TreeNode(1, TreeNode(0))),TreeNode(7, None, TreeNode(8)))
    k = 5

    #Act
    result = kth_smallest(root, k)

    #Assert
    assert result == 7

def test_kth_smallest_on_single_node_bst():
    #Arrange
    root = TreeNode(42, None, None)
    k = 1

    #Act
    result = kth_smallest(root,k)

    #Assert
    assert result == 42

