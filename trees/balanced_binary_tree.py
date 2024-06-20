from typing import Optional

# Given a binary tree, determine if it is height-balanced
# A height-balanced binary tree is a binary tree in which the depth of the
# two subtrees of every node never differs by more than one.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Your implementation here
        pass

# Example usage:
# Construct the binary tree
#     3
#    / \
#   9   20
#       / \
#      15  7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create a Solution object and test the method
solution = Solution()
print(solution.isBalanced(root))  # Expected output: True
