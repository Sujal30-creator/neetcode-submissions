# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        curr_diam = left_height + right_height

        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(curr_diam, left_diameter, right_diameter)