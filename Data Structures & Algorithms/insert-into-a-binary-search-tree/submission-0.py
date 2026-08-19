# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val=val, left=None, right=None)
            return root
        
        def findPrev(node, val):
            if node.val > val:
                if node.left:
                    findPrev(node.left, val)
                else:
                    node.left = TreeNode(val = val, left=None, right=None)
            elif node.val <= val:
                if node.right:
                    findPrev(node.right, val)
                else:
                    node.right = TreeNode( val = val, left = None, right=None)

        findPrev(root, val)
                
        return root