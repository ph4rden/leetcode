from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        A mistake I made was having a conditional to check if both the left and right child
        nodes existed, when every node should be processed regardless of its children.
        1. Define recursive function
        2. Provide base case
        3. Swap children
        4. Call function again on those children

        Time complexity:  O(n)  
        because each node in the tree is processed exactly once

        Space complexity:  O(h)  
        where h is the height of the tree, due to the recursion stack, 
        with a worst-case of O(n) and a best-case of O(log n).
        '''
        def switchNodes(rootNode): 
            if rootNode is None:
                return 
            rootNode.left, rootNode.right = rootNode.right, rootNode.left 
            switchNodes(rootNode.left)
            switchNodes(rootNode.right)
        
        switchNodes(root)
        return root

# Helper function to print the tree level by level (for better visualization)
def printTree(root):
    if root is None:
        print("Empty tree")
        return
    
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            print(node.val, end=' ')
            queue.append(node.left)
            queue.append(node.right)
        else:
            print("None", end=' ')
    print()

# Example usage
if __name__ == "__main__":
    # Create a sample tree: [1, 2, 3, None, None, 4, 5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    solution = Solution()
    
    print("Original tree:")
    printTree(root)
    
    inverted_root = solution.invertTree(root)
    
    print("Inverted tree:")
    printTree(inverted_root)