from typing import Optional

# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

'''
    thought process - 
    currently on a plane
    input: root of binary tree
    action: calculate diameter of binary tree (longest path between 2 nodes)
    output: length of the diameter of the tree

    maybe use depth first search?
    forgot the dfs algo... 
    traverse tree all the way down then increment by 1, get the max path of 
    the left and right side of the root note and add it together
'''

'''
    solution:
        - start from the bottom
        - find diameter and height for each node
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root): 
            if not root: 
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            
            return 1 + max(left, right)
        dfs(root)
        return res[0]
    
# Example usage:
# Construct the binary tree
#     1
#    / \
#   2   3
#  / \
# 4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# root = TreeNode(1)
# root.left = TreeNode(2)


# Create a Solution object and test the method
solution = Solution()
print(solution.diameterOfBinaryTree(root))  # Expected output: 3
