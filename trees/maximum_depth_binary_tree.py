from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverseTree(rootNode):
            if rootNode is None:
                return 0
            return 1 + max(traverseTree(rootNode.left), traverseTree(rootNode.right))

        return traverseTree(root)

# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree:
    #       3
    #      / \
    #     9   20
    #         /  \
    #        15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Create a Solution object and find the maximum depth of the tree
    solution = Solution()
    max_depth = solution.maxDepth(root)

    # Print the result
    print(f"The maximum depth of the binary tree is: {max_depth}")